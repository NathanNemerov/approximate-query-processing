import psycopg
from dotenv import load_dotenv
import os

load_dotenv()


selected_table = input("Enter the name of the table you would like to sample: ")

threshold = 1.0/int(input("Enter the value for n (get every nth value): "))

with psycopg.connect(os.getenv("DATABASE_CONNECTION_STRING")) as conn:
    with conn.cursor() as cur:
        cur.execute(f"""
        select * 
        from {selected_table} where RANDOM() < {threshold};
        """)

        results = cur.fetchall()

        cur.execute(
            f"""
            DROP TABLE IF EXISTS {selected_table}_sample
            """
        )

        cur.execute(
            f"""
            CREATE TABLE {selected_table}_sample (value double precision)
            """
        )

        for row in results:
            cur.execute(f'INSERT INTO {selected_table}_sample (value) VALUES (%s)', (row[0],))
        

    conn.commit()