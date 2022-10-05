from flask import Blueprint

name = 'v1'
bp = Blueprint(name, __name__, url_prefix=f"/{name}")
