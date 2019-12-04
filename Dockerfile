FROM python:3.7-slim

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN pip install -r requirements.txt

ENTRYPOINT ["gunicorn", "app:create_app", "-b", "0.0.0.0:5000"]
