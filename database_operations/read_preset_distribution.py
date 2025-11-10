import pandas as pd
import psycopg
from dotenv import load_dotenv
import os

load_dotenv()

with psycopg.connect(os.getenv("DATABASE_CONNECTION_STRING")) as conn:
    df = pd.read_sql("SELECT best_distribution FROM distribution_analysis ORDER BY analysis_date DESC", conn)
    print(df)

with psycopg.connect(os.getenv("DATABASE_CONNECTION_STRING")) as conn:
    data = pd.read_sql("SELECT value FROM skeweddata", conn)