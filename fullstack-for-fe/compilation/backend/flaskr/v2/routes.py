from flask import request, render_template, redirect, url_for, escape, g
from flaskr.v2 import bp, name
db = g.get('db2')

@bp.route('/<string:short_url>')
def redirect_to_long(short_url):
    long_url = get_long_url(short_url)
    if long_url:
        return redirect(long_url)
    return f'Short url {escape(short_url)} not found ):'


def get_long_url(short_url: str):
    long_url = None
    with db.conn() as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM url_data WHERE id = %s', (short_url, ))
        long_url = cur.fetch()[0]['long']
    return long_url


@bp.route('/urls/', methods=('POST', 'GET'))
def urls():
    if request.method == 'POST':
        long_url = f"https://{request.form['long_url']}"
        with db.conn() as conn:
            with conn.cursor() as cur:
                cur.execute('INSERT INTO url_data (long_url) VALUES(%s);', (long_url, ))
                conn.commit()
                url_data = {'long_url': long_url, 'short_url': cur.lastrowid}
    return render_template(f"{name}/index.html", url_data=url_data, action=url_for(f'{name}.urls'))

