from . import client


def test_xml2json(client):
    response = client.post('/convert/xml2json')
    assert response.status_code == 200
    assert response.data == b'xml2json'
