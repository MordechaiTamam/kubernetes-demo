#https://hub.docker.com/_/python
# Use an official Python runtime as a parent image
FROM python:3.8-slim

RUN pip3 install touch
# Set the working directory to /app
WORKDIR /app

# Copy score.py into the container as /app
COPY score.py .


# Run app.py when the container launches
CMD ["bash"]