from flaskr import app
from flask import Blueprint
import os
basedir = os.path.abspath(os.path.dirname(__file__))

name = 'v4'
bp = Blueprint(name, __name__, url_prefix=f"/{name}")

app.register_blueprint(bp)