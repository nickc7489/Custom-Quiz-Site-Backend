FROM python:3.8-alpine
ARG PYTHONBUFFERED 1
WORKDIR /quiz_handler
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .