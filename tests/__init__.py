import pytest
from mongoengine.connection import get_db, connect

import config
from app import create_app


@pytest.fixture
def client():
    """
    A pytest fixture that exposes the flask app test client.

    https://flask.palletsprojects.com/en/1.1.x/testing/
    """
    app = create_app()
    with app.test_client() as client:
        yield client

    db = connect(host=config.TEST_MONGODB_URL, alias="test")
    db.drop_database("test")
