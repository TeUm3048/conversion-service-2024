from flask import Blueprint, request, Response
from lxml import etree

convert = Blueprint('convert', __name__)


@convert.route('/json2xml', methods=['POST'])
def json2xml():
    
    return Response('json2xml', content_type='application/xml; charset=utf-8', mimetype='application/xml')


@convert.route('/xml2json', methods=['POST'])
def xml2json():
    data = request.get_data()
    data = etree.fromstring(data)
    data = etree.tostring(data, encoding='utf-8')
    
    return Response(data, content_type='text/xml; charset=utf-8', mimetype='application/xml')
