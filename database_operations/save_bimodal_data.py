#Imports 
import random
import psycopg

#region Copied data gen code from bimodal_generation.py

BIAS_ARRAY = [0.01, 0.02, 0.03, 0.1, 0.2, 0.2, 0.3, 0.3, 0.4, 0.5, 0.5, 0.6, 0.8, 1, 0.8, 0.6, 0.5, 0.5, 0.4, 0.3, 0.3, 0.2, 0.2, 0.1, 0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.2, 0.3, 0.3, 0.4, 0.5, 0.5, 0.6, 0.8, 1, 0.8, 0.6, 0.5, 0.5, 0.4, 0.3, 0.3, 0.2, 0.2, 0.1, 0, 0, 0]

BIAS_ARRAY_LEN = len(BIAS_ARRAY)


data_size = int(input("Enter an integer number of data points to generate: "))

random_array = []


for i in range(0, data_size):
    random_array.append(BIAS_ARRAY[int(BIAS_ARRAY_LEN * i/data_size)] * random.randrange(100, 110))

#endregion

with psycopg.connect("dbname=university user=python password=pythonConnection") as conn:
    #Create table and insert data
    with conn.cursor() as cur:
        # Uncomment the line below if you want to regenerate data
        # cur.execute("DROP TABLE bimodaldata")

        # Create table skeweddata and insert data
        cur.execute("CREATE TABLE bimodaldata (value double precision)")
        
        for num in random_array:
            cur.execute('INSERT INTO bimodaldata (value) VALUES (%s)', (num,))

        conn.commit()