import pandas as pd
import psycopg
import matplotlib.pyplot as plt
import numpy as np
from dotenv import load_dotenv
import os

load_dotenv()


with psycopg.connect(os.getenv("DATABASE_CONNECTION_STRING")) as conn:
    df = pd.read_sql("SELECT value FROM bimodaldata", conn)

data = df["value"].values

counts, bin_edges = np.histogram(data, bins=20)

freq_df = pd.DataFrame({
    "bin_start": bin_edges[:-1],
    "bin_end": bin_edges[1:],
    "frequency": counts
})

print(freq_df)

plt.figure(figsize=(8,4))
plt.hist(data, bins=20, edgecolor='black')
plt.title("Value Frequency Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()