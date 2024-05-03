import os
from datetime import datetime
from io import StringIO

import pandas as pd

from db.utils import execute_query, init_connection_engine


def parse_candidate_name(file_path: str) -> str:
    """

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The candidate's name in the format "First, Last".
    """
    try:
        first_name = file_path.split("_")[0].replace("submissions/", "").capitalize()
        last_name = file_path.split("_")[1].capitalize()

    except IndexError:
        raise ValueError(
            "Invalid file name format. Please use '{first_name}_{last_name}_sql_exercise_submission.sql'."
        )

    return f"{first_name} {last_name}"


def list_files(directory: str) -> list[str]:
    """List all files in a directory.

    Args:
        directory (str): The directory containing the files.

    Returns:
        list[str]: A list of file names in the directory.
    """
    with os.scandir(directory) as entries:
        return [f"{directory}/{entry.name}" for entry in entries if entry.is_file()]


def grade_submission(submission_file, solution_file):

    print(f"Grading {parse_candidate_name(submission_file)}'s submission...")

    # Connect to your database
    conn = init_connection_engine(dockerized=False)

    # Read and parse the SQL files
    with open(submission_file, "r") as file:
        # Splitting by semicolon for individual queries
        candidate_queries = file.read().split(";")
        # Remove whitespace and empty strings
        candidate_queries = [
            query.strip() for query in candidate_queries if query.strip()
        ]

    with open(solution_file, "r") as file:
        # Splitting by semicolon for individual queries
        solution_queries = file.read().split(";")
        # Remove whitespace and empty strings
        solution_queries = [
            query.strip() for query in solution_queries if query.strip()
        ]

    results = []
    for idx, (c_query, s_query) in enumerate(
        zip(candidate_queries, solution_queries), start=1
    ):
        try:
            # Execute the queries
            candidate_result = execute_query(conn, c_query)
            solution_result = execute_query(conn, s_query)

            # Compare the results and convert them to string for storing in DataFrame
            result = {
                "exercise_number": idx,
                "candidate_query": c_query,
                "solution_query": s_query,
                "candidate_query_output_head": candidate_result.head(5).to_csv(
                    index=False
                ),
                "expected_output_head": solution_result.head(5).to_csv(index=False),
                "candidate_query_output": candidate_result.to_csv(index=False),
                "expected_output": solution_result.to_csv(index=False),
                "result_match": candidate_result.equals(solution_result),
            }
            results.append(result)
        except Exception as e:
            results.append(
                {
                    "exercise_number": idx,
                    "candidate_query": c_query,
                    "solution_query": s_query,
                    "candidate_query_output_head": "Error",
                    "expected_output_head": "Error",
                    "candidate_query_output": "Error",
                    "expected_output": "Error",
                    "result_match": str(e),
                }
            )

    # Convert the list of results to a DataFrame
    results_df = pd.DataFrame(results)

    # Print out the % of exercises that were correct
    num_correct = results_df["result_match"].sum()
    total = len(results_df)
    print(f"Total correct: {num_correct}/{total} ({num_correct/total:.0%})")

    return results_df


def grade_and_save_submission(submission_file: str, solution_file: str) -> None:
    """Grade a SQL submission and save the results to a CSV file marked with the current timestamp in the "submissions" folder.

    Args:
        submission_file (str): The file path to the submission SQL file.
        solution_file (str): The file path to the solution SQL file.
    """

    graded_submission = grade_submission(submission_file, solution_file)

    try:
        # Change the file path to csv and include the current timestamp with underscores as separators
        now = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        file_id = submission_file.replace("submissions/", "").replace(
            "submission.sql", f"results_{now}.csv"
        )
        graded_submission_path = f"./graded_submissions/{file_id}"

        # Write the results to a CSV file inside of the "submissions" folder
        graded_submission.to_csv(graded_submission_path, index=False)

        print(f"Finished grading {parse_candidate_name(submission_file)}'s submission.")

    except Exception as e:
        print(f"An error occurred while saving the graded submission: {e}")
        return


# Function to convert a string back to a DataFrame
def string_to_df(data_string: str) -> pd.DataFrame:
    """Convert a string representation of a DataFrame to a DataFrame.

    Args:
        data_string (str): The string representation of a DataFrame.

    Returns:
        pd.DataFrame: The DataFrame
    """
    return pd.read_csv(StringIO(data_string))
