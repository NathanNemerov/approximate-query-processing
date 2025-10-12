import pandas as pd
import psycopg

with psycopg.connect("dbname=aqp_database user=postgres password=403754") as conn:
    df = pd.read_sql("SELECT best_distribution FROM distribution_analysis ORDER BY analysis_date DESC", conn)
    print(df)

with psycopg.connect("dbname=aqp_database user=postgres password=403754") as conn:
    data = pd.read_sql("SELECT value FROM skeweddata", conn)