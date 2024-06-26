<h1 align="center">Curri Data Engineering Internship Take Home Assignment</h1>

<p align="center">
  <a href="" rel="noopener">
  <img width=500px height=300px src="https://assets-global.website-files.com/63734c3e67347c96ff82a923/6373917c7edcfb1a116865ea_Curri%20Logotype.svg" alt="Project logo"></a>
</p>

<p align="center"> A take home assignment of SQL exercises for summer 2024 internship candidates </p>
    <br> 
</p>

## 📝 Table of Contents

* [📝 Table of Contents](#-table-of-contents-)
* [🧐 About](#-about-)
* [❗ Prerequisites](#-prerequisites-)
* [🧰 Setup](#-setup-)
* [🏁 Getting Started](#-getting-started-)
* [🚀 Submission](#-submission-)
* [🏋️ Exercises](#-exercises-)
* [🗂️ ERD](#-erd-)




## 🧐 About <a name = "about"></a>

This repository contains a take home assignment of SQL exercises for summer 2024 internship candidates. The assignment is divided into 2 parts:

1. SQL Theory -- Short answer theoretical questions about SQL and databases
2. SQL Exercises -- Write SQL queries to solve the exercises

The exercises are designed to test the candidate's SQL knowledge and problem solving skills. The candidate is expected to solve the exercises and submit the solutions in a text file and a SQL file.

## ❗ Prerequisites <a name = "prerequisites"></a>

Before you begin the setup section (below), you will need to have access to or create a new a GitHub account.

## 🧰 Setup <a name = "setup"></a>

To complete the assignment, you will need to have the following installed:
1. [Docker Desktop](https://www.docker.com/products/docker-desktop)
2. [DBeaver (Community/Open Source Version)](https://dbeaver.io/download/) (or another SQL client of your choice)
3. [Git](https://git-scm.com/downloads)


## 🏁 Getting Started <a name = "getting-started"></a>

### Step 1: Clone the Repository
Open your terminal and run the following command to clone the repository to your local machine:

```bash
git clone https://github.com/teamcurri/sql-exercises.git
```

### Step 2: Make sure Docker is running
Open Docker Desktop and make sure it is running. If it is not running, start it.

To check if Docker is running, you can run the following command in your terminal:

```bash
docker info
```

You should see information about your Docker installation if it is running, something like this:

```
Client:
 Version:    26.0.0
 Context:    desktop-linux
 Debug Mode: false
 Plugins:
  buildx: Docker Buildx (Docker Inc.)
  ...
```

### Step 3: Start the Database
Navigate to the repository directory (in the same terminal window)

```bash
cd sql-exercises
```

Run the following command to start the database:

```bash
docker-compose up -d
```

This might take a few minutes to create and populate the database.

### Step 4: Connect to the Database
Open DBeaver (or another SQL client of your choice) and connect to the database using the following credentials:

```bash
host=localhost
port=5432
database=curri-practice-db
user=curri
```

### Step 5: Connecting to the Database and Writing Queries

Connecting to the Database:


https://github.com/teamcurri/sql-exercises/assets/62448274/619ff1d6-b701-4fc6-be07-e7dec3e7f66a



Writing Queries:


https://github.com/teamcurri/sql-exercises/assets/62448274/a29a4cfc-b216-4b55-98a4-859d8ee680d9




### Step 6: Complete the Exercises

For the coding exercises, write out all of your SQL queries in a single file called `{first_name}_{last_name}_sql_exercise_submission.sql`. You can use DBeaver or another SQL client to write and execute/test your queries.

Please make sure to include a semi-colon `;` at the end of each query.

For the short answer questions, write out your answers in a text file called `{first_name}_{last_name}_sql_theory_submission.txt` and make sure to include the question number before each answer.

## 🚀 Submission <a name = "submission"></a>

To submit your solutions, send over the `{first_name}_{last_name}_sql_exercise_submission.sql` file and the `{first_name}_{last_name}_sql_theory_submission.txt` file as a DM in Slack to **@Nathan Jones**.

If you have any questions or need help with the assignment, please reach out in Slack.

Good luck! 🚀

## 🏋️ Exercises <a name = "exercises"></a>

### Theoretical Questions

1. What is a primary key? What is a foreign key? How are they different?

2. What is the difference between the order of execution of the clauses in a SQL query and the order of appearance of the clauses in a SQL query? (`SELECT`, `FROM`, `WHERE`, `GROUP BY`, `ORDER BY`)

3. Briefly explain what a `LEFT JOIN` is, a `RIGHT JOIN` is, and an `INNER JOIN` is. Match each of these join types with the correct Venn diagram representation below. (For example, "Join scenario A is an example of a `_____ JOIN`")

![SQLVD](./readme_images/sql-join-venn-diagrams.png)

4. What is a "one-to-many" relationship?

5. Your friend Nathan is telling you that he joined the `orders` onto the `drivers` table using each table's `driver_id` column. Nathan can't figure out why he is seeing multiple entries for the same driver in his result set. How would you explain the issue to Nathan?

### Coding Exercises

**Note**: The *Expected Output* for exercises without a sorting will not match your output exactly (which is fine). The expected output is just a sample of what the output should look like. The *Expected Output* for exercises with sorting will match your output exactly.

**Question 1.** List all orders with their associated id, order times, product names, quantities, and order statuses. Sort the list so the oldest orders appear first.

**Expected Output:**

| order_id | ordered_at                | name           | quantity | status    |
| -------: | :------------------------ | :------------- | -------: | :-------- |
|     8319 | 2024-01-01 00:28:25+00:00 | Salad          |        2 | Delivered |
|    11691 | 2024-01-01 00:36:29+00:00 | Burger         |        1 | Delivered |
|    13552 | 2024-01-01 00:44:25+00:00 | Salad          |        2 | Delivered |
|    12314 | 2024-01-01 00:56:08+00:00 | Soup           |        1 | Delivered |
|     9645 | 2024-01-01 01:08:57+00:00 | Chocolate Cake |        4 | Pending   |
|      ... | ...                       | ...            |      ... | ...       |

**Question 2.** Find the total number of orders for each user that has placed an order. Include the user's id, name, and the total number of orders. Sort the results by the user's with the most orders. Name the columns `user_id`, `user_name`, and `total_orders`.

**Expected Output:**

| user_id | user_name         | total_orders |
| ------: | :---------------- | -----------: |
|      37 | Alexander Collins |           96 |
|     178 | Thomas Johnston   |           96 |
|      54 | Kyle Preston      |           94 |
|      93 | Renee Bruce       |           94 |
|      31 | Randy Shah        |           93 |
|     ... | ...               |          ... |


**Question 3.** Calculate the total revenue generated by each product, sorted by revenue. Name the columns `product_name` and `total_revenue`.

**Expected Output:**

| product_name   |      total_revenue |
| :------------- | -----------------: |
| Soup           | 106729.23999999856 |
| Mac and Cheese | 105695.70000000215 |
| Salad          |  90594.12000000001 |
| Pancakes       |  68141.67000000017 |
| Burger         |  66629.82000000094 |
| ...            |                ... |


**Question 4.** List all products and their last delivery date. Name the columns `product_name` and `latest_delivery_date`.

**Expected Output:**

| product_name   | latest_delivery_date      |
| :------------- | :------------------------ |
| Burger         | 2024-12-31 06:34:39+00:00 |
| Vegan Bowl     | 2024-12-30 22:58:49+00:00 |
| Mac and Cheese | 2024-12-31 15:54:15+00:00 |
| Pasta          | 2024-12-31 19:45:55+00:00 |
| Burrito        | 2024-12-30 06:21:06+00:00 |
| ...            | ...                       |

**Question 5.** Find the number of orders each driver has been assigned to. If there are drivers that have not been assigned to a delivery, make sure they show up and have 0 for their order count. Name the columns `driver_id`, `name`, and `order_count`.

**Expected Output:**

|   driver_id | name            |   order_count |
|------------:|:----------------|--------------:|
|          23 | John Pierce     |           661 |
|          24 | Melissa Marquez |             0 |
|          11 | Amy Underwood   |           662 |
|           8 | Jamie Chavez    |           643 |
|          19 | Ashley Garrett  |           653 |
| ...         | ...             |           ... |

**Question 6.** Calculate the average time to complete a delivery (in hours) for orders that have been delivered. Name the column `average_delivery_hours`.

**Expected Output:**

|   average_delivery_hours |
|-------------------------:|
|                  12.6198 |

**Question 7.** Show the total orders and total pending orders for each city where drivers are based.

**Expected Output:**

| address_city   |   total_orders |   pending_orders |
|:---------------|---------------:|-----------------:|
| Lake Curtis    |            644 |               36 |
| Riceside       |            655 |               25 |
| Lake Mark      |            637 |               34 |
| Traciebury     |            621 |               26 |
| East Nathaniel |            653 |               30 |


## 🗂️ ERD <a name = "erd"></a>

Here is the Entity Relationship Diagram (ERD) for the practice database. You can use this to understand the relationships between the tables and it will help you write your queries.

![ERD](./readme_images/curri-practice-db.png)
