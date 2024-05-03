import datetime
import random

import pandas as pd
from sqlalchemy import Engine, create_engine

# Set seed
random.seed(42)


def init_connection_engine(dockerized=True) -> Engine:
    """Initializes a connection to a PostgreSQL database.

    Returns:
        Engine: The database engine you can use to interact with the database.
    """
    # Connect to the database
    try:
        if dockerized:
            conn_string = (
                f"postgresql://curri@host.docker.internal:5432/curri-practice-db"
            )
        else:
            conn_string = f"postgresql://curri@localhost:5432/curri-practice-db"
        engine = create_engine(url=conn_string)

    except Exception as e:
        print(f"Error connecting to the database: {e}")

    return engine


def execute_query(connection, query) -> pd.DataFrame:
    """Execute a SQL query against a database.

    Args:
        connection (sqlalchemy.Engine): A sqlalchemy connection object.
        query (str): A SQL query as a string.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the result of the SQL query.
    """
    return pd.read_sql(query, connection)


def fixed_date_time_this_year():
    """Generate a datetime object for the same year, starting from a fixed date."""
    base_date = datetime.datetime(2024, 1, 1)  # Example: start of 2024
    end_date = datetime.datetime(2024, 12, 31)  # End of 2024
    time_delta = end_date - base_date
    seconds_in_year = time_delta.total_seconds()
    random_second = random.randint(0, int(seconds_in_year))
    return base_date + datetime.timedelta(seconds=random_second)
