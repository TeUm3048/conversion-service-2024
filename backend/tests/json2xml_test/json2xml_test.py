from .. import client
from lxml import etree
import json
import pytest
from app.schemas.add_entrant_json import AddEntrantSchema


def test_valid_json_schema(json_entrant):
    AddEntrantSchema.model_validate_json(json.dumps(json_entrant))


def test_headers(client, json_entrant):
    response = client.post("/convert/json2xml", data=json.dumps(json_entrant),
                           content_type='application/json')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert response.mimetype == 'application/json'


@pytest.mark.skip(reason='not implemented')
def test_valid_xml_schema(client, json_entrant, xml_schema):
    response = client.post("/convert/json2xml", data=json_entrant,
                           content_type='application/json')
    assert xml_schema.validate(etree.fromstring(response.data))


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
