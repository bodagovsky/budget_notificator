FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

COPY db/password.txt db/password.txt
COPY db/migrations db/migrations

CMD [ "python3", "main.py"]