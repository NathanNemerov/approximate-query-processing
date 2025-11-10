import pandas as pd
import psycopg
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from dotenv import load_dotenv
import os

load_dotenv()

with psycopg.connect(os.getenv("DATABASE_CONNECTION_STRING")) as conn:
    df = pd.read_sql("SELECT value FROM skeweddata", conn)

data = df["value"].values

# Remove any NaN or infinite values or 0's
data = data[np.isfinite(data)]
data = data[data > 0]
data_clipped = np.clip(data, np.percentile(data, 0.1), np.percentile(data, 99.9))

# Data log helps exagerate the numbers for more specificity, sort of like MLE
# data_log = np.log(data_clipped + 1e-9)
# print(df.describe())
# print(np.max(data), np.min(data))

distributions = [
    'norm',
    'expon',
    'lognorm',
    'uniform',
    'gamma',
    'beta',
    'chi2',
    'logistic',
    'weibull_min',
    'weibull_max',
]
results = {}

for dist_name in distributions:
    try:
        dist = getattr(stats, dist_name)
        params = dist.fit(data_clipped)
        with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
            ks_stat, ks_p = stats.kstest(data_clipped, dist_name, params)
        
        if np.isfinite(ks_stat) and np.isfinite(ks_p):
            results[dist_name] = {'ks_stat': ks_stat, 'ks_p': ks_p, 'params': params}
        else:
            print(f"Skipping {dist_name} due to numerical issues")
            
    except Exception as e:
        print(f"Failed to fit {dist_name}: {e}")
        continue

best_fit = max(results, key=lambda x: results[x]['ks_p'])
print(f"Best fit: {best_fit}, KS p-value: {results[best_fit]['ks_p']}")

with psycopg.connect(os.getenv("DATABASE_CONNECTION_STRING")) as conn:
    with conn.cursor() as cur:
        # Create table if it doesn't exist
        cur.execute("""
            CREATE TABLE IF NOT EXISTS distribution_analysis (
                id SERIAL PRIMARY KEY,
                analysis_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                best_distribution VARCHAR(50),
                ks_p_value FLOAT,
                ks_statistic FLOAT,
                distribution_params TEXT,
                data_size INTEGER
            )
        """)
        
        params_str = str(results[best_fit]['params'])
        all_results_json = {k: {
            'ks_stat': float(v['ks_stat']), 
            'ks_p': float(v['ks_p']), 
            'params': [float(p) for p in v['params']]
        } for k, v in results.items()}
        
        cur.execute("""
            INSERT INTO distribution_analysis 
            (best_distribution, ks_p_value, ks_statistic, distribution_params, data_size)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            best_fit,
            float(results[best_fit]['ks_p']),
            float(results[best_fit]['ks_stat']),
            params_str,
            len(data_clipped)
        ))
        
        conn.commit()
