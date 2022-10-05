from flaskr import app
from flask import Blueprint

name = 'v3'
bp = Blueprint(name, __name__, url_prefix=f"/{name}")

app.register_blueprint(bp)
