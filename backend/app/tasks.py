from celery import shared_task
from .models import AddEntrant, AddEntrantAddress
from .database import SessionLocal
from .schemas.add_entrant_xml import AddEntrantXMLSchema
from .schemas.add_entrant_json import AddEntrantSchema
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task(ignore_result=False)
def save_entrant(data: AddEntrantXMLSchema):
    logger.info('Saving entrant')

    with SessionLocal() as db:
        ent = AddEntrant.from_xml_schema(data)
        db.add(ent)
        db.commit()
        logger.info(f'Entrant {ent.id} saved')
    return ent.id


@shared_task(ignore_result=False)
def convert_entrant_to_json(data: AddEntrantXMLSchema) -> AddEntrantSchema:
    logger.info('Converting XML entrant to JSON')
    ent = AddEntrantSchema.from_xml_schema(data)
    return ent
