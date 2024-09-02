import pytest
from lxml import etree
from .. import client


def test_xml2json(client, xml_valide_pass_rus):
    response = client.post('/convert/xml2json',
                           content_type='text/xml', data=xml_valide_pass_rus)
    assert response.status_code == 200


def test_valide_post_data_with_schema(xml_valide_pass_rus, xml_schema):
    data = etree.fromstring(xml_valide_pass_rus)
    assert xml_schema.validate(data)


def test_valide_exist_entrant_with_schema(xml_exist_entrant, xml_schema):
    data = etree.fromstring(xml_exist_entrant)
    assert xml_schema.validate(data)


@pytest.fixture()
def xml_valide_pass_rus():
    with open('tests/xml2json_test/assets/AddNewEntrantPassRUS.xml', 'r') as file:
        xml_data = file.read()

    return xml_data.encode("utf-8")


@pytest.fixture()
def xml_exist_entrant():
    with open('tests/xml2json_test/assets/ExistEntrant.xml', 'r') as file:
        xml_data = file.read()

    return xml_data.encode("utf-8")


@pytest.fixture()
def xml_schema():
    schema = etree.XMLSchema(etree.parse(
        'tests/xml2json_test/assets/Add_Entrant_List.xsd'))
    return schema
