from flask import request, render_template, redirect, url_for, escape, g
from flaskr import app
db = g.get('db')

@app.route('/<string:short_url>')
def redirect_to_long(short_url):
    long_url = get_long_url(short_url)
    if long_url:
        return redirect(long_url)
    return f'Short url {escape(short_url)} not found ):'


def get_long_url(short_url: str):
    with db.conn() as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM url_data WHERE id = %s', (short_url, ))
        return cur.fetch()[0]['long']


@app.route('/urls/', methods=('POST', 'GET'))
def urls():
    url_data = {}
    if request.method == 'POST':
        url_data = save_url(request.form['long_url'])
    return render_template("index.html", url_data=url_data, action=url_for('urls'))


def save_url(long_url: str):
    long_url = f"https://{long_url}"
    with db.conn() as conn:
        with conn.cursor() as cur:
            cur.execute('INSERT INTO url_data (long_url) VALUES(%s);', (long_url, ))
            conn.commit()
            return {'long_url': long_url, 'short_url': cur.lastrowid}