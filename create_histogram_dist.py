import pandas as pd
import psycopg
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

with psycopg.connect("dbname=university user=postgres password=403754") as conn:
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

counts, bin_edges = np.histogram(data_clipped, bins=20)

freq_df = pd.DataFrame({
    "bin_start": bin_edges[:-1],
    "bin_end": bin_edges[1:],
    "frequency": counts
})

print(freq_df)

plt.figure(figsize=(8,4))
plt.hist(data_clipped, bins=20, edgecolor='black')
plt.title("Value Frequency Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()