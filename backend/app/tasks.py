from celery import shared_task
from pydantic import ValidationError
from .models import AddEntrantModel, EntrantJson
from .database import SessionLocal
from .schemas.add_entrant_xml import AddEntrantXMLSchema
from .schemas.add_entrant_json import AddEntrantSchema
from .schemas.get_entrant_xml import PackageDataXMLSchema, create_get_entrant_xml_response
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task(ignore_result=False)
def save_entrant(data: AddEntrantXMLSchema):
    logger.info('Saving entrant')

    with SessionLocal() as db:
        ent = AddEntrantModel.from_xml_schema(data)
        db.add(ent)
        db.commit()
        logger.info(f'Entrant {ent.id} saved')
    return ent.id


@shared_task(ignore_result=False)
def convert_entrant_to_json(data: AddEntrantXMLSchema) -> AddEntrantSchema:
    logger.info('Converting XML entrant to JSON')
    ent = AddEntrantSchema.from_xml_schema(data)
    return ent.model_dump_json()


@shared_task(ignore_result=False)
def convert_entrant_to_xml(data: AddEntrantSchema) -> PackageDataXMLSchema:
    logger.info('Converting JSON entrant to XML')
    try:
        result = create_get_entrant_xml_response(data)
    except ValidationError as e:
        logger.error(f'Error converting JSON entrant to XML: {e}')
        raise
    return result.to_xml()


@shared_task(ignore_result=False)
def save_entrant_json(data: AddEntrantSchema):
    logger.info('Saving entrant from JSON')
    with SessionLocal() as db:
        ent = EntrantJson.from_schema(data)
        db.add(ent)
        db.commit()
        logger.info(f'Entrant {ent.id} saved')
    return ent.id
