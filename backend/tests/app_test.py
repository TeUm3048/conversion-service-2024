import pytest
from . import client


def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello!'
