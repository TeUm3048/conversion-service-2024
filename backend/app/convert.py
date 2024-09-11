from celery import shared_task
from flask import Blueprint, jsonify, request, Response
from lxml import etree
from .schemas.xml import parse_xml, add_entrant_parser
from .schemas.add_entrant_xml import EntrantChoiceXMLSchema, AddEntrantXMLSchema, ExistEntrantXMLSchema
from .schemas.add_entrant_json import AddEntrantSchema
from .tasks import save_entrant, convert_entrant_to_json, convert_entrant_to_xml, save_entrant_json
from pydantic import ValidationError
convert = Blueprint('convert', __name__)


@convert.route('/json2xml', methods=['POST'])
def json2xml():
    data = request.get_data()
    try:
        ent = AddEntrantSchema.model_validate_json(data)
    except ValidationError as e:
        return jsonify({'error': str(e)}), 400
    save_task_id = save_entrant_json.delay(ent).id
    convert_task_id = convert_entrant_to_xml.delay(ent).id
    return jsonify({'save_task_id': save_task_id, 'convert_task_id': convert_task_id})


@convert.route('/xml2json', methods=['POST'])
def xml2json():
    data = request.get_data()
    try:
        root = EntrantChoiceXMLSchema.from_xml(data)
    except etree.XMLSyntaxError as e:
        return jsonify({'error': str(e)}), 400
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

    match root.choice:
        case _ as entrant if isinstance(entrant, AddEntrantXMLSchema):
            save_task_id = save_entrant.delay(entrant).id
            convert_task_id = convert_entrant_to_json.delay(entrant).id
            return jsonify({'save_task_id': save_task_id, 'convert_task_id': convert_task_id})
        case _ as existed if isinstance(existed, ExistEntrantXMLSchema):
            return jsonify(existed)


@convert.route('/xml2json/<task_id>', methods=['GET'])
def get_json(task_id):
    task = convert_entrant_to_json.AsyncResult(task_id)
    if task.state == 'SUCCESS':
        return jsonify(task.result)
    return jsonify({'state': task.state})
