import psycopg
from dotenv import load_dotenv
import os
from distribution_analysis import distribution_analysis
import numpy as np

load_dotenv()


selected_table = input("Enter the name of the table you would like to sample: ")

threshold = 1.0/int(input("Enter the scalar for selection: "))

with psycopg.connect(os.getenv("DATABASE_CONNECTION_STRING")) as conn:
    with conn.cursor() as cur:

        cur.execute(
            f"""
                select distribution_params from distribution_analysis where table_name = \'{selected_table}\'
            """
        )

        if cur.fetchone() is None:
            print("No distribution analysis has been run on this table. Running analysis...")
            distribution_analysis(selected_table)
            print("Analysis complete.")
        else:
            if input("Analysis on this data has been found. Would you like to run a new analysis? (Y/n)").lower() == 'y':
                print("Beginning analysis.")
                distribution_analysis(selected_table)
                print("Analysis complete.")

        cur.execute(
            f"""
                select distribution_params from distribution_analysis where table_name = \'{selected_table}\'
            """
            )
        

        dist_params = cur.fetchone()[0]

        avg, stddev = eval(dist_params)

        print("The first parameter is ", avg)


        cur.execute(
            f"""
            select value from bimodaldata b where RANDOM() < {threshold}/ ABS((value - {avg})/{stddev});
            """
        )

        results = cur.fetchall()

        cur.execute(
            f"""
            DROP TABLE IF EXISTS {selected_table}_biased_sample
            """
        )

        cur.execute(
            f"""
            CREATE TABLE {selected_table}_biased_sample (value double precision)
            """
        )

        for row in results:
            cur.execute(f'INSERT INTO {selected_table}_biased_sample (value) VALUES (%s)', (row[0],))
        

    conn.commit()