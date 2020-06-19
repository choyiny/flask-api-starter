# Boilerplate for Flask APIs
A skeleton Flask API only application to quickstart development.

## Features
- Uses [Flask Blueprints](https://flask.palletsprojects.com/en/1.1.x/blueprints/) for module separation
- Support for PostgreSQL connection
- Database migrations with [Alembic](https://alembic.sqlalchemy.org/en/latest/)
- Fully dockerized and deployment ready
- ORM-ready with [SQLAlchemy](https://www.sqlalchemy.org/)
- Various (optional) helper classes with common useful functionality
- [CORS](https://flask-cors.readthedocs.io/en/latest/) protected
- Integrates with [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/) and [Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)
- [Sentry](https://sentry.io/) Integration
- Documentation generated with [Flask-APISpec](https://github.com/jmcarp/flask-apispec/)
- [Celery](http://www.celeryproject.org/) worker queue support.

## Deployment
`Dockerfile` is ready for deployment.
It is recommended to reverse proxy through nginx.

## Development
### Setup

Note: This project *requires* Python 3.7+ installed. For Mac users, ensure you are using the correct version of Python because the OS preinstalls Python 2.7 and default `pip` and `python` commands execute in v2.7 rather than v3.x.

1. Create a virtual environment for the project and activate it. Run `pip3 install virtualenv` if virtualenv is not installed on Python3.7+
    ```
    $ virtualenv flask-starter-venv --python=python
    $ source flask-starter-venv/bin/activate
    ```

3. Clone the repository to your directory
    ```
    (flask-starter-venv) $ git@github.com:choyiny/flask-api-starter.git
    ```

4. Install the required dependencies
    ```
    (flask-starter-venv) $ cd flask-api-starter
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
    
### Database Setup
Alembic is used to manage database migrations. Existing migrations are version controlled so to generate migrations after making changes to any models,
 
1. Ensure models are imported in `flask-api-starter/extensions.py`.
2. Generate the migrations
    ```
    (flask-starter-venv) $ flask db migrate -m "migration message."
    ```
3. Edit the migrations if necessary.
4. Migrate the database.
    ```
    (flask-starter-venv) $ flask db upgrade
    ```

### Setting up Blueprints
Flask blueprints are like modules. To create a new one, you can copy the example blueprint, and modify the `__init__.py`
to change the prefix url. Ensure that it is also included in `app.py`.
    
## Managing Utilities
Resetting database
```
(flask-starter-venv) $ python manage.py resetdb
```
Seeding the database
```
(flask-starter-venv) $ python manage.py seedfile seed
```
