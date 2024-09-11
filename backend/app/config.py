import os
import json


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

    SECRET_KEY = 'dev'

    CELERY = dict(
        broker_url=os.environ.get('CELERY_BROKER_URL'),
        result_backend=os.environ.get('CELERY_RESULT_BACKEND'),
        task_ignore_result=True,

    )

    CELERY_TASK_SERIALIZER = os.environ.get('CELERY_TASK_SERIALIZER')

    CELERY_RESULT_SERIALIZER = os.environ.get('CELERY_RESULT_SERIALIZER')

    try:
        CELERY_ACCEPT_CONTENT = json.loads(
            os.environ.get('CELERY_ACCEPT_CONTENT'))
    except json.JSONDecodeError:
        raise ValueError("""CELERY_ACCEPT_CONTENT must be a valid JSON string.
            Example: ["json", "pickle"]. Don\'t forget to use double quotes for strings.""")


def sdf():
    pass
