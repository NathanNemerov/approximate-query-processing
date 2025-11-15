import psycopg
from dotenv import load_dotenv
import os

load_dotenv()


selected_table = input("Enter the name of the table you would like to sample: ")


with psycopg.connect(os.getenv("DATABASE_CONNECTION_STRING")) as conn:
    with conn.cursor() as cur:
        cur.execute(f"""
        select AVG(value)
        from {selected_table};
        """)
    
        print(cur.fetchone())

        

    conn.commit()