FROM python:3.8-slim

EXPOSE 8081

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

CMD gunicorn myteacher.wsgi:application -b 0.0.0.0:8081
