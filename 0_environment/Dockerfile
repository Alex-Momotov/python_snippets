# This is an example of how Dockerfile can look like when using pipenv inside a container

# Start with python 3.7 image.
FROM python:3.7

# Copy Pipfile, Pipfile.lock and our script to the container.
COPY Pipfile* ./
COPY my_script.py ./

# Install pipenv onto the system, using system python's 'pip'.
RUN pip install pipenv

# Install packages specified in Pipfile.lock onto system's python interpreter.
# --system          Uses system's Python installation instead of creating a virt env.
#                   Since we are already in a Docker container, we already have isolation from the host OS and there is no need to create another virt env.
# --deploy          Abort if Pipfile.lock is out of date, or Python version is wrong.
# --ignore-pipfile  Builds environment using Pipfile.lock instead of Pipfile. Results in deterministic virt env build.
RUN pipenv install --system --deploy --ignore-pipfile

# Run your script.
CMD ["python3", "my_script.py"]

