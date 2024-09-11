from datetime import date
from uuid import UUID
import flask
import pytest
from lxml import etree
from .. import client
from app.schemas.add_entrant_xml import EntrantChoiceXMLSchema


def test_headers(client, xml_valide_pass_rus_entrant):
    response = client.post('/convert/xml2json',
                           content_type='text/xml', data=xml_valide_pass_rus_entrant)
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert response.mimetype == 'application/json'


def test_invalide_post_data(client):
    response = client.post('/convert/xml2json',
                           content_type='text/xml', data=b'')
    assert response.status_code == 400


@pytest.mark.skip(reason='not implemented')
def test_json_data(client, xml_valide_pass_rus_entrant):
    response = client.post('/convert/xml2json',
                           content_type='text/xml; charset=utf-8', data=xml_valide_pass_rus_entrant)
    data = response.json
    assert data == {
        'name': 'Иван',
        'surname': 'Иванов',
        'patronymic': 'Иванович',
        'birth_date': '01.01.1990',
        'passport_type_id': '1',
        'passport_series': '4509',
        'passport_number': '123456',
        'passport_begda': '01.01.2010',
        'passport_issued_by': 'ОВД района Центральный',
        'passport_org_code': '123-456',
        'citizenship_id': '1',
        'tel_mobile': '8-800-555-35-35',
        'email': 'entrant@example.com',
        'motherland': 'г. Москва',
        'dict_sex_id': '1',
        'snils': '123-456-789 01'
    }


def test_valide_post_data_with_schema(xml_valide_pass_rus_entrant, xml_schema):
    data = etree.fromstring(xml_valide_pass_rus_entrant)
    assert xml_schema.validate(data)


def test_valide_exist_entrant_with_schema(xml_exist_entrant, xml_schema):
    data = etree.fromstring(xml_exist_entrant)
    assert xml_schema.validate(data)


def test_valide_pydantic_model(xml_valide_pass_rus_entrant):
    data = etree.fromstring(xml_valide_pass_rus_entrant)
    # add_entrant = EntrantChoice.from_xml(xml_valide_pass_rus_entrant)
    add_entrant = EntrantChoiceXMLSchema.from_xml_tree(data)
    assert add_entrant.model_dump() == {"choice": {
        'addresses': [
            {
                'city': 'Москва',
                'full_address': 'Россия, г. Москва, ул. Пушкина, д. 1',
                'id_region': 77,
                'is_registration': True
            },
            {
                'city': 'Санкт-Петербург',
                'full_address': 'Россия, г. Санкт-Петербург, ул. Ленина, д. 5',
                'id_region': 78,
                'is_registration': False,
            },
        ],
        'identification': {
            'id_document_type': 1,
            'doc_name': 'Паспорт гражданина РФ',
            'doc_series': '4509',
            'doc_number': '123456',
            'issue_date': date(2015, 7, 1),
            'issue_by': 'ОВД района Центральный',
            'fields': {
                'subdivision_code': '770-001',
                'id_oksm': 643,
                'surname': 'Иванов',
                'name': 'Иван',
                'patronymic': 'Иванович'
            }
        },
        'birthday': date(1990, 1, 1),
        'birthplace': 'г. Москва',
        'email': 'entrant@example.com',
        'free_education_reason': {'id_free_education_reason': 1,
                                  'id_oksm_free_education_reason': 840},
        'id_gender': 1,
        'id_oksm': 643,
        'snils': '12345678901',
        'phone': '+7(800)555-35-35',
    }}


# @pytest.mark.skip(reason='not implemented')
def test_valide_pydantic_model_from_dict(xml_valide_pass_rus_entrant, xml_schema, dict_pass_rus_entrant):
    add_entrant = EntrantChoiceXMLSchema.model_validate(dict_pass_rus_entrant)
    xml_schema.assertValid(add_entrant.to_xml_tree())


def test_valide_pydantic_model_exist_entrant(xml_exist_entrant):
    data = etree.fromstring(xml_exist_entrant)
    add_entrant = EntrantChoiceXMLSchema.from_xml(xml_exist_entrant)
    assert add_entrant.model_dump() == {'choice': {'guid': UUID(
        '123e4567-e89b-12d3-a456-426614174000')}}


@pytest.fixture()
def dict_pass_rus_entrant():
    return {"choice": {
        'addresses': [
            {
                'city': 'Москва',
                'full_address': 'Россия, г. Москва, ул. Пушкина, д. 1',
                'id_region': 77,
                'is_registration': True
            },
            {
                'city': 'Санкт-Петербург',
                'full_address': 'Россия, г. Санкт-Петербург, ул. Ленина, д. 5',
                'id_region': 78,
                'is_registration': False,
            },
        ],
        'identification': {
            'id_document_type': 1,
            'doc_name': 'Паспорт гражданина РФ',
            'doc_series': '4509',
            'doc_number': '123456',
            'issue_date': date(2015, 7, 1),
            'issue_by': 'ОВД района Центральный',
            'fields': {
                'subdivision_code': '123-456',
                'id_oksm': 643,
                'surname': 'Иванов',
                'name': 'Иван',
                'patronymic': 'Иванович'
            }
        },
        'birthday': date(1990, 1, 1),
        'birthplace': 'г. Москва',
        'email': 'entrant@example.com',
        'free_education_reason': {'id_free_education_reason': 1,
                                  'id_oksm_free_education_reason': 840},
        'id_gender': 1,
        'id_oksm': 643,
        'snils': '12345678901',
        'phone': '+7(800)555-35-35',
    }}


@pytest.fixture()
def xml_valide_pass_rus_entrant():
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
