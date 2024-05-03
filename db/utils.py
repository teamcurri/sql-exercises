from typing import List

import pandas as pd
from sqlalchemy import Engine, create_engine


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
