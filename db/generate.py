import random
from datetime import timedelta

import pandas as pd
from faker import Faker

# Initialize Faker
fake = Faker()

# Set the seed for reproducibility
Faker.seed(42)
random.seed(42)

# Define a custom list of product names
PRODUCT_NAME_LIST = [
    "Pizza",
    "Burger",
    "Salad",
    "Sushi",
    "Pasta",
    "Tacos",
    "Steak",
    "Soup",
    "Sandwich",
    "Curry",
    "Vegan Bowl",
    "Falafel",
    "Dumplings",
    "Chocolate Cake",
    "Ice Cream",
    "Mac and Cheese",
    "Burrito",
    "Fish and Chips",
    "Pancakes",
    "Fried Rice",
]


def generate_product_data(num_products: int) -> pd.DataFrame:
    """Generate fake product data.

    Args:
        num_products (int): Number of products to generate.

    Returns:
        pd.DataFrame: A DataFrame containing the generated product data. Columns are "name", "price_dollars", and "cost_dollars".
    """
    # Ensure the list has at least as many items as `num_products`
    assert (
        len(PRODUCT_NAME_LIST) >= num_products
    ), "Please add more products to the `PRODUCT_NAME_LIST` list."

    # Generate products
    products = [
        (
            fake.random_element(elements=PRODUCT_NAME_LIST),
            round(random.uniform(2, 20), 2),
            round(random.uniform(1, 10), 2),
        )
        for i in range(num_products)
    ]
    return pd.DataFrame(products, columns=["name", "price_dollars", "cost_dollars"])


def generate_user_data(num_users: int) -> pd.DataFrame:
    """Generate fake user data.

    Args:
        num_users (int): Number of users to generate.

    Returns:
        pd.DataFrame: A DataFrame containing the generated user data. Columns are "name", "email", "address_state_code", and "address_city".
    """

    # Generate users
    users = [
        (fake.name(), fake.email(), fake.state_abbr(), fake.city())
        for i in range(num_users)
    ]

    return pd.DataFrame(
        users, columns=["name", "email", "address_state_code", "address_city"]
    )


def generate_driver_data(num_drivers: int) -> pd.DataFrame:
    """Generate fake driver data.

    Args:
        num_drivers (int): Number of drivers to generate.

    Returns:
        pd.DataFrame: A DataFrame containing the generated driver data. Columns are "name", "address_state_code", and "address_city".
    """
    # Generate drivers
    drivers = [
        (fake.name(), fake.state_abbr(), fake.city()) for i in range(num_drivers)
    ]
    return pd.DataFrame(drivers, columns=["name", "address_state_code", "address_city"])


def generate_order_data(
    num_orders: int, num_users: int, num_drivers: int, num_products: int
) -> pd.DataFrame:
    """Generate fake order data.

    Args:
        num_orders (int): Number of orders to generate.
        num_users (int): Number of users to generate.
        num_drivers (int): Number of drivers to generate.
        num_products (int): Number of products to generate.

    Returns:
        pd.DataFrame: A DataFrame containing the generated order data. Columns are "user_id", "driver_id", "product_id", "quantity", "ordered_at", "delivered_at", and "status".
    """
    # Generate orders
    orders = []
    for i in range(num_orders):
        user_id = random.randint(1, num_users)
        driver_id = random.randint(1, num_drivers)
        product_id = random.randint(1, num_products)
        quantity = random.randint(1, 5)  # Assuming 1-5 quantity per order
        ordered_at = fake.date_time_this_year()

        # 95% chance of being delivered
        delivered = random.choices([True, False], weights=[0.95, 0.05])[0]

        if delivered:
            # Add a random time delta to `ordered_at` to simulate delivery time
            delivered_at = ordered_at + timedelta(hours=random.randint(1, 24))
            status = "Delivered"
        else:
            delivered_at = None  # No delivery time if not delivered
            status = "Pending"

        orders.append(
            (
                user_id,
                driver_id,
                product_id,
                quantity,
                ordered_at.isoformat(),
                delivered_at.isoformat() if delivered_at else None,
                status,
            )
        )
    df = pd.DataFrame(
        orders,
        columns=[
            "user_id",
            "driver_id",
            "product_id",
            "quantity",
            "ordered_at",
            "delivered_at",
            "status",
        ],
    )
    df["ordered_at"] = pd.to_datetime(df["ordered_at"], utc=True)
    df["delivered_at"] = pd.to_datetime(df["delivered_at"], utc=True)
    return df
