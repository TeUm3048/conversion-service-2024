from . import client


def test_json2xml(client):
    response = client.post('/convert/json2xml')
    assert response.status_code == 200
    assert response.data == b'json2xml'
