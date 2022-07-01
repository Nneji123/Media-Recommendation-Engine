FROM python:3.8-slim-buster

WORKDIR /app

RUN apt-get -y update  && apt-get install -y \
  python3-dev \
  apt-utils \
  python-dev \
  build-essential \
&& rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade setuptools 
    

COPY requirements_api.txt .
RUN pip install -r requirements_api.txt

COPY . .

CMD uvicorn api:app --reload --port 5000