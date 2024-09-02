import pytest
from app import flask_app



@pytest.fixture()
def client():
    client = flask_app.test_client()
    return client

