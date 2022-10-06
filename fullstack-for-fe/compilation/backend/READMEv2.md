# TinyUrl clone

## Spec

1. A user can submit a "long" url to get a shortened url
2. When that shortened url is pasted into the browser the browser will be redirected to the original "long" url site

## Versions

- This codebase incrementally improves all versions of the code are active at the same time
- As to not repeat code, some improvements will require commenting/uncommenting edits

## Setup

- Clone this repo
- `cd backend`
  - the root of this codebase
- `python3 -m venv venv`
  - Create a python virtual environment (v-env)
- `. venv/bin/activate`
  - Activate that venv, if you run `which pip` it should point to `<path_of_venv>/bin/pip`
- `pip install -e .`
  - -e Tells pip to find setup.py in the current directory and install it in editable or development mode. Editable mode means that as you make changes to your local code, you’ll only need to re-install if you change the metadata about the project, such as its dependencies.
- `export FLASK_APP=flaskr && export FLASK_DEBUG=true && flask run`
  - We need to tell flask where our python module code is, the `__init__.py` file makes /flaskr a module
  - By enabling debug mode, the server will automatically reload if code changes, and will show an interactive debugger in the browser if an error occurs during a request.
- Visit `localhost:5000` in browser
  - Should return "Hello, World!"
- In Vscode download the Python extension by Microsoft
- Alternatively, to run with pycharm
  - Top right -> Edit configurations -> flask server
  - Target type [X], script path, select `flaskr/wsgi.py`
  - FLASK_ENV = development, FLASK_DEBUG [X]

## General notes

- When running the `flaskr/wsgi.py` the `__init__.py` will run prior. Note the single global `app` instance that will be used throughout the other parts of the code
  - Ex. in `wsgi.py` note `@app.route("/")`
  - This says, create a GET(default) route that just returns a 200 status + text
- **Templates**: files that contain static data as well as placeholders for dynamic data. A template is rendered with specific data to produce a final document
  - [Dynamic data example](https://flask.palletsprojects.com/en/2.2.x/tutorial/templates/#id1)
  - Flask renders (fills out the dynamic parts of the template) prior to return this view to the client
  - All templates reside in the /templates folder by default
- **Blueprints**: a way to organize a group of related views and other code. Rather than registering views and other code directly with an application, they are registered with a blueprint
  - Typically used to organize features, [ex. register and login](https://flask.palletsprojects.com/en/2.2.x/tutorial/views/) but we use it to organize our code versions, i.e. v1, v2, etc...
  - Views of a feature often resides in its own /feature_name sub-folder in templates but all our code versions use the same index.html view
- All routes of the blueprint must be "loaded" prior to registration

## V1

- Uses an url.json file for storing the urls
- Browse `localhost:5000/v1/urls/`, submit an url, and ensure the app works

## V2

- Uses a Sqlite, an SQL database engine meant to run on devices such as mobile phones, as opposed meant running on a server by itself

- [Sql alchemy](https://www.compose.com/articles/using-postgresql-through-sqlalchemy/)
- testdriven.io
  - https://testdriven.io/courses/tdd-flask/
  - https://testdriven.io/courses/aws-flask-react/intro/
  - https://testdriven.io/courses/scalable-flask-aws/
- [CORS](https://flask-cors.readthedocs.io/en/latest/)
- [Restful](https://flask-restful.readthedocs.io/en/latest/quickstart.html)
- [Awesome flask p1](https://github.com/humiaozuzu/awesome-flask)
- [Awesome flask p2](https://github.com/mjhea0/awesome-flask)
- [SqlAlchemy](https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/)
- [digital ocean](https://www.digitalocean.com/community/tutorials/how-to-use-a-postgresql-database-in-a-flask-application)
  - `pip install psycopg2-binary`
  - `export DB_USERNAME= && export DB_PASSWORD=`
- `docker run --name my-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d --rm postgres:13.0`
- `docker exec -it -u postgres my-postgres psql`

- [Sql designer](https://ondras.zarovi.cz/sql/demo/)
- `export FLASK_APP=app.py && flask db init`
- `flask db migrate -m "url table"`
  - generate migrate script
- `flask db upgrade`
  - apply migrations
- `flask db downgrade`
  - undos last migration

Restful + sqlalchemy

- https://blog.j-labs.pl/flask-restful-with-sqlalchemy
- https://rahmanfadhil.com/flask-rest-api/

* marsh

- https://realpython.com/flask-connexion-rest-api-part-2/
- https://towardsdev.com/create-a-rest-api-in-python-with-flask-and-sqlalchemy-e4839cd61ddd
