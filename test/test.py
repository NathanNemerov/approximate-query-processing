import psycopg

with psycopg.connect("dbname=university user=python password=pythonConnection") as conn:
    
    # Open a cursor to perform database operations
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM teaches")
        for record in cur:
            print(record)

        conn.commit()