import os

from flask import Flask, request
from celery import Celery, Task

from .tasks import add_task
from .convert import convert


def celery_init_app(app: Flask) -> Celery:

    class ContextTask(Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name, task_cls=ContextTask)

    celery_app.config_from_object(app.config)

    celery_app.set_default()  # Крайне важна строчка, иначе не будет работать

    # Add celery to app.extensions to access it later by app.extensions['celery']
    app.extensions['celery'] = celery_app

    return celery_app


def create_app(test_config=None) -> tuple[Flask, Celery]:
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # TODO: Change this to a real database
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        CELERY=dict(
            broker_url='CELERY_BROKER_URL',
            result_backend='CELERY_RESULT_BACKEND',
            task_ignore_result=True
        )
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    # TODO: Delete this if database is not sqlite
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.config.from_prefixed_env()

    celery = celery_init_app(app)

    return app, celery


flask_app, celery_app = create_app()

flask_app.register_blueprint(convert, url_prefix='/convert')


@flask_app.post('/')
def hello():
    a = request.form.get('a', type=int)
    b = request.form.get('b', type=int)
    result = add_task.delay(a, b)
    return {'task_id': result.id}
