import psycopg2
from psycopg2 import extras
from psycopg2.extensions import register_adapter, AsIs
import numpy as np
import argparse
import pandas as pd

DB_PARAMS = {
    "dbname": "postgres",
    "user": "postgres",
    "host": "127.0.0.1",
    "port": "5432",
}

register_adapter(np.int64, AsIs)


def connect_to_db() -> tuple:
    """
    Connect to the database
    :return connection and cursor
    """
    conn = psycopg2.connect(**DB_PARAMS)
    cursor = conn.cursor()
    return conn, cursor


def _exists_table(cursor, table_name: str):
    cursor.execute(
        "SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = %s)",
        (table_name,),
    )
    table_exists = cursor.fetchone()[0]
    return table_exists


def _drop_table(cursor, table_name: str):
    cursor.execute(f"DROP TABLE {table_name}")


def drop_tables() -> None:
    conn, cursor = connect_to_db()

    for table_name in ["frappe", "frappe_raw"]:
        if _exists_table(cursor, table_name):
            _drop_table(cursor, table_name)
        conn.commit()

    conn.close()


def create_tables() -> None:
    conn, cursor = connect_to_db()

    for table_name in ["frappe", "frappe_raw"]:
        if not _exists_table(cursor, table_name):
            cursor.execute(
                f"CREATE TABLE {table_name} ("
                "id SERIAL PRIMARY KEY,"
                "label INTEGER,"
                "feature1 INTEGER,"
                "feature2 INTEGER,"
                "feature3 INTEGER,"
                "feature4 INTEGER,"
                "feature5 INTEGER,"
                "feature6 INTEGER,"
                "feature7 INTEGER,"
                "feature8 INTEGER,"
                "feature9 INTEGER,"
                "feature10 INTEGER"
                ")",
            )
            conn.commit()
    conn.close()


def prepare_data(number_of_rows) -> None:
    """
    Prepare data for the experiment. Two tables are created: frappe and frappe_raw. frappe_raw contains the original data,
     and frappe contains the data for the experiment.
    :param number_of_rows: number of rows in frappe table
    :return None
    """
    conn, cursor = connect_to_db()

    # ******* frappe table *******
    cursor.execute("SELECT COUNT(*) FROM frappe")
    current_row_num = cursor.fetchone()[0]

    if current_row_num > number_of_rows:
        raise Exception(
            f"Number of rows in frappe table is {current_row_num}, greater than {number_of_rows}"
        )

    # insert data into the frappe table
    data = pd.read_csv("dataset/frappe.csv")
    data = data.sample(n=number_of_rows - current_row_num, replace=True)
    insert_query = "INSERT INTO frappe (label, feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, feature9, feature10) VALUES %s"
    # convert numpy.int64 to int
    data = data.astype(int)
    extras.execute_values(cursor, insert_query, data.values)
    conn.commit()
    cursor.execute("SELECT COUNT(*) FROM frappe")
    print(f"Number of rows in frappe table: {cursor.fetchone()[0]}")

    # ******* frappe_raw table *******
    data = pd.read_csv("dataset/frappe.csv")
    insert_query = "INSERT INTO frappe_raw (label, feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, feature9, feature10) VALUES %s"
    # convert numpy.int64 to int
    data = data.astype(int)
    extras.execute_values(cursor, insert_query, data.values)
    conn.commit()
    cursor.execute("SELECT COUNT(*) FROM frappe_raw")
    print(f"Number of rows in frappe_raw table: {cursor.fetchone()[0]}")
    conn.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--drop_tables",
        action="store_true",
        help="Drop the frappe and frappe_raw tables",
    )
    parser.add_argument(
        "--create_tables",
        action="store_true",
        help="Create the frappe and frappe_raw tables",
    )
    parser.add_argument(
        "--num_rows", type=int, default=10000, help="Number of rows in the frappe table"
    )
    args = parser.parse_args()

    if args.drop_tables:
        drop_tables()

    if args.create_tables:
        create_tables()

    prepare_data(args.num_rows)
