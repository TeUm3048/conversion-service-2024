import os

from flask import Flask, request, abort, jsonify
from .convert import convert


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # TODO: Change this to a real database
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
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

    return app


app = create_app()

app.register_blueprint(convert, url_prefix='/convert')


@app.route('/')
def hello():
    return "Hello!"


print(app.url_map)
if __name__ == '__main__':
    app.run()
