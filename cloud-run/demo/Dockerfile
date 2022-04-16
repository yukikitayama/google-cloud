# https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service

# https://hub.docker.com/_/python
FROM python:3.10

ENV PYTHONUNBUFFERED True

# Copy files in a directory where this Dockerfile exists
# e.g. requirements.txt for Python package installation
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Python docker image uses Debian, so if you wanna install
# Linux system packages, then do here
# We need --yes to force it to yes everything because
# we cannot intervene during deployment
# RUN apt-get update
# RUN apt-get install --yes SOME_SYSTEM_PACKAGE

# Install Python dependency to run Python code if necessary
RUN pip install -r requirements.txt

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
