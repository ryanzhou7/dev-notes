from flask import Blueprint, request, render_template, redirect, url_for, escape
import psycopg2
import os

name = 'v3'
bp = Blueprint(name, __name__, url_prefix=f"/{name}")


def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='postgres',
                            user=os.environ['DB_USERNAME'] or 'postgres',
                            password=os.environ['DB_PASSWORD'] or 'mysecretpassword'
                            )
    return conn


@bp.route('/')
def index():
    return redirect(url_for(f'{name}.urls'))


@bp.route('/<string:short_url>')
def redirect_to_long(short_url):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM url_data WHERE id = %s', (short_url,))
    row = cur.fetchall()
    cur.close()
    conn.close()
    print(row)
    help(row)
    url_data = row
    help(url_data)
    if url_data is None:
        return f'Short url {escape(short_url)} not found ):'
    else:
        return redirect(url_data[0]['long'])


@bp.route('/urls/', methods=('POST', 'GET'))
def urls():
    url_data = {}
    if request.method == 'POST':
        long_url = f"https://{request.form['long_url']}"
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute('INSERT INTO url_data (long_url) VALUES(%s);', (long_url,))
                conn.commit()
                url_data = {'long_url': long_url, 'short_url': cur.lastrowid}
    return render_template(f"{name}/index.html", url_data=url_data, action=url_for(f'{name}.urls'))
