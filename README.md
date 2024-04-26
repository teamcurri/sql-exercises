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
* [🧰 Setup] (#-setup-)
* [🏁 Getting Started](#-getting-started-)
* [🚀 Submission](#-submission-)





## 🧐 About <a name = "about"></a>

This repository contains a take home assignment of SQL exercises for summer 2024 internship candidates. The assignment is divided into 2 parts:

1. SQL Exercises -- Write SQL queries to solve the exercises
2. SQL Theory -- Short answer theoretical questions about SQL and databases

The exercises are designed to test the candidate's SQL knowledge and problem solving skills. The candidate is expected to solve the exercises and submit the solutions in a SQL file.

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
git clone {repository-url}
```

### Step 2: Start the Database
Navigate to the repository directory (in the same terminal window)

```bash
cd sql-exercises
```

Run the following command to start the database:

```bash
docker-compose up -d
```

### Step 3: Connect to the Database
Open DBeaver (or another SQL client of your choice) and connect to the database using the following credentials:

- Host: localhost
- Port: 5432
- Database: curri-practice-db
- User: 

### Step 4: Complete the Exercises
Write out all of your SQL queries in a single file called `{first_name}_{last_name}_sql_exercise_submission.sql`. You can use DBeaver or another SQL client to write and test your queries.

## 🚀 Submission <a name = "submission"></a>
To submit your solutions, send over the `{first_name}_{last_name}_sql_exercise_submission.sql` file via email to nathan.jones@curri.com.

For the subject line of the email, please use the following format: `Curri Data Engineering Internship Take Home Assignment Submission - {First Name} {Last Name}`

If you have any questions or need help with the assignment, please reach out in the #summer-2024-data-internship channel on Slack.

Good luck! 🚀

## 📝 TODO
- [ ] Add exercises to the README
  - Theoretical Questions
  - SQL Exercises
- [ ] Add more data to the practice database
- [ ] Add an ERD for the practice database
- [ ] Add `head()` of expected output for each exercise's solution