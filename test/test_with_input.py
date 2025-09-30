import psycopg

with psycopg.connect("dbname=university user=python password=pythonConnection") as conn:
    # Open a cursor to perform database operations
    query = input("Enter a query (type \"exit\" to quit): ")
    while query != "exit":
        with conn.cursor() as cur:
                try:
                    cur.execute(query)
                    for record in cur:
                        print(record)
                    query = input("Enter another query: ")
                except Exception as e:
                    print(e)
                    query = input("Query invalid. Try another: ")

        conn.commit()