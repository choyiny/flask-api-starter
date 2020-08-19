# Boilerplate for Flask APIs
A skeleton Flask API only application to quickstart development.

## Features
- Uses [Flask Blueprints](https://flask.palletsprojects.com/en/1.1.x/blueprints/) for module separation
- ORM-ready with mongoengine and MongoDB.
- Fully dockerized and deployment ready
- [CORS](https://flask-cors.readthedocs.io/en/latest/) protected
- Integrates with [Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)
- [Sentry](https://sentry.io/) Integration
- Documentation generated with [Flask-APISpec](https://github.com/jmcarp/flask-apispec/)
- [Celery](http://www.celeryproject.org/) worker queue support.

## Deployment
`Dockerfile` is ready for deployment.
It is recommended to reverse proxy through nginx.

## Development
### Setup

Note: This project *requires* Python 3.7+ installed. For Mac users, ensure you are using the correct version of Python because the OS preinstalls Python 2.7 and default `pip` and `python` commands execute in v2.7 rather than v3.x.

1. Clone this repo or create a new one with this as a template.

1. Create a virtual environment for the project and activate it. Run `pip3 install virtualenv` if virtualenv is not installed on Python3.7+
    ```
    $ cd flask-api-starter  # or your repo name
    $ virtualenv venv --python=python
    $ source venv/bin/activate
    ```

4. Install the required dependencies, and setup automatic code quality checking with `black`.
    ```
    (flask-starter-venv) $ pip install -r requirements.txt
    (flask-starter-venv) $ pip install -r requirements-dev.txt
    (flask-starter-venv) $ pre-commit install
    ```

5. Edit `config.py.bak` with the proper credentials and move it to `config.py`.
6. Run Migrations
    ```
    (flask-starter-venv) $ flask db upgrade
    ```
    
### Run Locally
Remember to fill any necessary fields in `config.py`.
1. Make sure you are in your virtualenv that you setup
    ```
    $ source flask-starter-venv/bin/activate
    ```
2. Start server
    ```
    (flask-starter-venv) $ flask run
    ```
3. Start Celery worker
    ```
    (flask-starter-venv) $ celery worker -A worker.celery --loglevel=info
    ```
    
### Setting up Blueprints
Flask blueprints are like modules. To create a new one, you can copy the example blueprint, and modify the `__init__.py`
to change the prefix url. Ensure that it is also included in `app.py`.
