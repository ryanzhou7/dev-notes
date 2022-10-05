import sqlite3
import click
from flask import current_app, g

from flaskr import v3

def init_app(app):
    app.cli.add_command(init_db_command)


@v3.bp.cli.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_postgres()


def get_db():
    if 'db3' not in g:
        g.db2 = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db2.row_factory = sqlite3.Row

    return g.db2

def init_postgres():
    """Clear the existing data and create new tables."""

    # Open a cursor to perform database operations
    conn = v3.get_db_connection()
    cur = conn.cursor()
    with current_app.open_resource('schema.sql') as f:
        cur.execute(f.read().decode('utf8'))
        conn.commit()
        cur.close()
        conn.close()
        click.echo('Initialized the database.')
