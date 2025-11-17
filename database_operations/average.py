import psycopg
from dotenv import load_dotenv
import os
import time


load_dotenv()

selected_table = input("Enter the name of the table you'd like to compare the averages of: ")

with psycopg.connect(os.getenv("DATABASE_CONNECTION_STRING")) as conn:
    with conn.cursor() as cur:
        print("-------------- Averages -------------------")
        full_data_start = time.perf_counter()
        cur.execute(
        f"""
        select avg(value) from {selected_table}
        """
        )
        full_data_end = time.perf_counter()
        full_data_runtime = full_data_end - full_data_start
        true_average = cur.fetchone()[0]
        print("True average: ", true_average)

        try:
            random_start = time.perf_counter()
            cur.execute(
            f"""
            select avg(value) from {selected_table}_sample
            """
            )
            random_end = time.perf_counter()
            random_runtime = random_end - random_start
            random_sample_average = cur.fetchone()[0]
            print("Random sample average: ", random_sample_average)
        except:
            print("No random sample data found.")
        try:
            biased_start = time.perf_counter()
            cur.execute(
            f"""
            select avg(value) from {selected_table}_biased_sample
            """
            )
            biased_end = time.perf_counter()
            biased_runtime = biased_end - biased_start
            biased_sample_average = cur.fetchone()[0]
            print("Biased sample average: ", biased_sample_average)
        except:
            print("No biased sample data found.")
        


    print("-------------- Run time -------------------")

    print(f"Full data runtime: {full_data_runtime:.6f}")
    print(f"Random data runtime: {random_runtime:.6f}")
    print(f"Biased data runtime: {biased_runtime:.6f}")
    print(f"Difference between full and random data: {(full_data_runtime - random_runtime):.6f}")
    print(f"Difference between full and biased data: {(full_data_runtime - biased_runtime):.6f}")

    print("-------------- Errors -------------------")

    random_error = ((true_average - random_sample_average)/true_average) * 100
    biased_error = ((true_average - biased_sample_average)/true_average) * 100

    print(f"The random sample was off by: {random_error}%")
    print(f"The biased sample was off by: {biased_error}%")

    if(abs(random_error) > abs(biased_error)):
        print(f"The biased sample was better by {abs(random_error) - abs(biased_error)}%")
    else:
        print(f"The random sample was better by {abs(biased_error) - abs(random_error)}%")
    