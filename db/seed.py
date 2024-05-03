import pandas as pd
from generate import (
    generate_driver_data,
    generate_order_data,
    generate_product_data,
    generate_user_data,
)
from sqlalchemy import text
from utils import init_connection_engine

# Number of entries to generate
num_users = 200
num_products = 20
num_drivers = 25
num_orders = 15000

# Generate DataFrames
try:
    driver_data = generate_driver_data(num_drivers)
    order_data = generate_order_data(num_orders, num_users, num_drivers, num_products)
    product_data = generate_product_data(num_products)
    user_data = generate_user_data(num_users)
    print("Data generated successfully.")
except Exception as e:
    print(f"Error generating data: {e}")

# Connect to the database
engine = init_connection_engine()

# Write DataFrames to the database
try:
    # Create lists to iterate over
    df_list = [driver_data, order_data, product_data, user_data]
    pkey_list = ["driver_id", "order_id", "product_id", "user_id"]
    table_name_list = ["drivers", "orders", "products", "users"]

    for df, pkey, table_name in zip(df_list, pkey_list, table_name_list):
        # Increment index by 1 to start at 1 instead of 0
        df.index += 1
        # Write DataFrames to the database
        df.to_sql(
            table_name, con=engine, index=True, index_label=pkey, if_exists="fail"
        )
        # Add primary key constraints
        with engine.connect() as connection:
            connection.execute(
                text(f"ALTER TABLE {table_name} ADD PRIMARY KEY ({pkey});")
            )
            connection.commit()
    print("DataFrames written to the database successfully.")

except Exception as e:
    print(f"Error writing DataFrames to the database: {e}")
