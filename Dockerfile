FROM python:3.8-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip

WORKDIR /code

RUN apt-get update \
    && apt-get -y install libpq-dev gcc 
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt

COPY . /code/
