from flask import Blueprint

convert = Blueprint('convert', __name__)


@convert.route('/json2xml', methods=['POST'])
def json2xml():
    return 'json2xml'


@convert.route('/xml2json', methods=['POST'])
def xml2json():
    return 'xml2json'
