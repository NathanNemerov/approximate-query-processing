import pandas as pd
import psycopg
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import json

with psycopg.connect("dbname=university user=postgres password=403754") as conn:
    df = pd.read_sql("SELECT best_distribution FROM distribution_analysis ORDER BY analysis_date DESC", conn)
    print(df)