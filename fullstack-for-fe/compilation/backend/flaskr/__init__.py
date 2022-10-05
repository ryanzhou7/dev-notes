from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_object(Config)

# app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'app.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # silence the deprecation warning

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# import routes to load then before bp registering
from flaskr.v1 import routes as v1routes, bp as v1bp
app.register_blueprint(v1bp)

# from flaskr.v2 import routes
# from flaskr.v3 import routes
# from flaskr.v4 import routes, models

"""
export POSTGRES_USER=postgres && export POSTGRES_PW=mysecretpassword && export POSTGRES_URL=localhost:5432 && export POSTGRES_DB=postgres
"""
DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user='postgres',pw='mysecretpassword',url='localhost:5432',db='postgres')


# v3
# app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning


