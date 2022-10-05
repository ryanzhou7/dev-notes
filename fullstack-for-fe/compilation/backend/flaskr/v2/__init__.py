from flask import Blueprint
from flaskr import app
import os

name = 'v2'
bp = Blueprint(name, __name__, url_prefix=f"/{name}")

app.register_blueprint(bp)

# v2
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
)

app.config.from_pyfile('config.py', silent=True)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass