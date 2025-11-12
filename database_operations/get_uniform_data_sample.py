import psycopg
from dotenv import load_dotenv
import os

load_dotenv()


selected_table = "bimodaldata"

threshold = 1.0/int(input("Enter the value for n (get every nth value): "))

with psycopg.connect(os.getenv("DATABASE_CONNECTION_STRING")) as conn:
    with conn.cursor() as cur:
        cur.execute(f"""
        select * 
        from {selected_table} where RANDOM() < {threshold};
        """)

        for row in cur.fetchall():
            print(row)

    conn.commit()