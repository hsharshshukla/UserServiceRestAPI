FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

ENV PYTHONUNBUFFERED=1

COPY . ./

CMD [ "python3" ,"manage.py","runserver","0.0.0.0:8000"]
