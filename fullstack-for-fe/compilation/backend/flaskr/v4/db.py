import sqlite3
import click
from flask import current_app, g

from flaskr import v4

def init_app(app):
    app.cli.add_command(init_db_command)


@v4.bp.cli.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""



def get_db():
    if 'db4' not in g:
        g.db4 = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db4.row_factory = sqlite3.Row

    return g.db4