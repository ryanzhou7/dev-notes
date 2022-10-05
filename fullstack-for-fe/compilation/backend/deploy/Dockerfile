FROM python:slim

RUN useradd wsgi

WORKDIR /home/wsgi

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY wsgi wsgi
COPY migrations migrations
COPY wsgi.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP wsgi.py

RUN chown -R wsgi:wsgi ./
USER wsgi

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]