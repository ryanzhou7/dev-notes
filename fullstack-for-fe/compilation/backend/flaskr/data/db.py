import sqlite3
import click
from flask import current_app, g
from flaskr import data

from flaskr import app
import os

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

name = 'db2'

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


@data.bp.cli.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    with current_app.open_resource('schema.sql') as f:
        get_db().executescript(f.read().decode('utf8'))
    click.echo('Initialized the database.')


def get_db():
    if name not in g:
        g.db2 = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db2.row_factory = sqlite3.Row
    return g.db2


def close_db(e=None):
    db = g.pop(name, None)
    if db is not None:
        db.close()


def query_db(query, args=(), one=False):
    """ https://flask.palletsprojects.com/en/2.2.x/patterns/sqlite3/?highlight=sqlite """
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv
