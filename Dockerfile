# Dockerfile for a python numpy application
# This Dockerfile sets up a minimal Python environment with numpy installed
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY /NumPy-Cheat-sheets /NumPy-Cheat-sheets
COPY Numpy1_Tutorial/ Numpy1_Tutorial/
COPY Numpy2_Random/ Numpy2_Random/
COPY Numpy3_ufuncs/ Numpy3_ufuncs/
COPY codedex_numpy.py .
COPY codeharry_numpy.py .

# Install numpy
RUN pip install numpy

#default command to run when the container starts
CMD ["python", "codedex_numpy.py"]


