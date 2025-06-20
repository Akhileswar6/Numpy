# Dockerfile for a python numpy application
# This Dockerfile sets up a minimal Python environment with numpy installed
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY Numpy1_Tutorial/ Numpy1_Tutorial/
COPY run_all.py .


# Install numpy
RUN pip install numpy

#default command to run when the container starts
CMD ["python", "run_all.py"]


