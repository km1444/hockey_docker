FROM python:3.10-slim

RUN mkdir /app

COPY requirements.txt /app

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY hockey/ /app

WORKDIR /app

CMD ["gunicorn", "hockey.wsgi:application", "--bind", "0:8000" ]
