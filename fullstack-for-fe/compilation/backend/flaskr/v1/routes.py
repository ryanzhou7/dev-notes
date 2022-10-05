from flask import request, render_template, redirect, url_for
from markupsafe import escape
import json
import os.path
from . import name, bp


@bp.route('/<string:short_url>')
def redirect_to_long(short_url):
    long_url = get_long_url(short_url)
    if long_url:
        return redirect(long_url)
    return f'Short url {escape(short_url)} not found ):'


def get_long_url(short_url: str):
    if os.path.exists('urls.json'):
        with open('urls.json') as url_storage:
            urls = json.load(url_storage)
            if short_url in urls.keys():
                return urls[short_url]
    return None


@bp.route('/urls/', methods=('POST', 'GET'))
def urls():
    url_data = {}
    if request.method == 'POST':
        url_data = save_url(request.form['long_url'])
    return render_template("index.html", url_data=url_data, action=url_for(f'{name}.urls'))


def save_url(long_url: str):
    prefixed_long_url = f"https://{long_url}"
    urls = {}
    if os.path.exists('urls.json'):
        with open('urls.json') as url_storage:
            urls = json.load(url_storage)
    id_next = len(urls)
    urls[id_next] = prefixed_long_url
    with open('urls.json', 'w') as url_storage:
        json.dump(urls, url_storage)
    return {'long_url': prefixed_long_url, 'short_url': id_next}
