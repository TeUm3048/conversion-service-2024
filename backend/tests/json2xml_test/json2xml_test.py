from .. import client
from lxml import etree
import json
import pytest


def test_headers(response):
    assert response.status_code == 200
    assert response.content_type == 'application/xml; charset=utf-8'
    assert response.mimetype == 'application/xml'

@pytest.mark.skip(reason='not implemented')
def test_valide_schema(response, xml_schema):
    assert xml_schema.validate(etree.fromstring(response.data))


@pytest.fixture()
def response(client, json_entrant):
    response = client.post("/convert/json2xml", data=json_entrant,
                           content_type='application/json')
    return response


@pytest.fixture()
def json_entrant():
    with open('tests/json2xml_test/assets/user.json', 'r') as f:
        entrant = json.load(f)
    return entrant


@pytest.fixture()
def xml_schema():
    schema = etree.XMLSchema(etree.parse(
        'tests/json2xml_test/assets/Get_Entrant_List.xsd'))

    return schema
