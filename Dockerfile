# Use the official Python image from Docker Hub
# FROM gcr.io/kaggle-images/python # this took too long
FROM python:3.13-slim

# Set the working directory inside the container
WORKDIR /kaggle

# Install common utilities
RUN apt-get update && apt-get install -y procps less vim curl wget net-tools iputils-ping graphviz

# Install Python packages
COPY docker/requirements.txt docker/
RUN pip install --no-cache-dir -r docker/requirements.txt

# Set the PYTHONSTARTUP environment variable
ENV PYTHONSTARTUP=/kaggle/docker/py_package_imports.py

# create log directory
RUN mkdir -p /kaggle/log

# Copy some files into the container
COPY jupyter/start_jupyter.sh jupyter/
RUN chmod +x jupyter/start_jupyter.sh

# Copy your project files into the container
COPY . .

RUN echo "alias jc='jupyter console --existing'" >> ~/.bashrc && \
    echo "source ~/.bashrc" >> ~/.bash_profile

# Set the default command to run when the container starts
CMD ["/bin/bash"]
