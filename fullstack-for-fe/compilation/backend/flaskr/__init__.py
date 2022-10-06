from flask import Flask
from config import Config
import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_object(Config)

from flaskr import routes

