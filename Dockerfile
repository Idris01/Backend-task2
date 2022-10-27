FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 80

CMD gunicorn -w 2  --bind 0.0.0.0:80 wsgi:app
