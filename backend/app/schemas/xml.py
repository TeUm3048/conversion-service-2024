from lxml import etree, objectify


def get_schema(path: str) -> etree.XMLSchema:
    return etree.XMLSchema(etree.parse(path))


def get_parser(path: str) -> etree.XMLParser:
    return objectify.makeparser(schema=get_schema(path))


def parse_xml(data: bytes, parser: etree.XMLParser) -> objectify.ObjectifiedElement:
    root =  etree.fromstring(data, parser)
    return root


add_entrant_schema = get_schema('app/schemas/Add_Entrant_List.xsd')
add_entrant_parser = get_parser('app/schemas/Add_Entrant_List.xsd')


