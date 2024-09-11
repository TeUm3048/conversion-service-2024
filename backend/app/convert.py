from celery import shared_task
from flask import Blueprint, jsonify, request, Response
from lxml import etree
from .schemas.xml import parse_xml, add_entrant_parser
from .schemas.add_entrant_xml import EntrantChoiceXMLSchema, AddEntrantXMLSchema, ExistEntrantXMLSchema
from .tasks import save_entrant, convert_entrant_to_json
convert = Blueprint('convert', __name__)


@convert.route('/json2xml', methods=['POST'])
def json2xml():

    return Response('json2xml', content_type='application/xml; charset=utf-8', mimetype='application/xml')


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
