import os

from grade.submissions import grade_and_save_submission, list_files

# Directory path to the submissions
directory_path = "submissions"

# Create the directory if it doesn't exist
if not os.path.exists(directory_path):
    os.makedirs(directory_path)

# List all files in the directory
submission_files = list_files(directory_path)

# Grade each submission
solution_file = "exercise_solutions.sql"
for submission_file in submission_files:
    grade_and_save_submission(submission_file, solution_file)
