# Use an official Python runtime as a parent image
FROM python:3.11

# Copy the current directory contents into the container
COPY . .

# Install Poetry and pin the version
RUN pip install poetry==1.7.1

### Configure Poetry and install dependencies
# Set the environment variable to disable virtualenv creation
ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_CACHE_DIR=/tmp/poetry_cache

 # Configure Poetry
RUN poetry config virtualenvs.in-project false

# Install dependencies and when deploying add `&& rm -rf $POETRY_CACHE_DIR` to remove the cache (don't need in docker image and this makes the image smaller)
RUN poetry install --no-interaction --no-ansi --no-root
