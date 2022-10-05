- [Official docs](https://flask.palletsprojects.com/en/2.2.x/)
- `python3 -m venv venv`
- `. venv/bin/activate`
- `pip install Flask==2.2`
- paste hello world into hello.py
- `flask --app app run`
- `flask --app app --debug run`

  - "By enabling debug mode, the server will automatically reload if code changes, and will show an interactive debugger in the browser if an error occurs during a request."

- `export FLASK_APP=flaskr && export FLASK_DEBUG=true && flask run`
- pycharm
  - flask server
  - script path, target = flaskr/app.py
- `flask --app flaskr init-db`

  - See instance .sqlite

- `pip install -e .`
  - Tells pip to find setup.py in the current directory and install it in editable or development mode. Editable mode means that as you make changes to your local code, you’ll only need to re-install if you change the metadata about the project, such as its dependencies.

[Deploy to prod](https://flask.palletsprojects.com/en/2.2.x/tutorial/deploy/)

- `pip install wheel`
- `python setup.py bdist_wheel`
- gunicorn
- `flask run --port 5001`

https://github.com/pallets/flask/tree/main/examples/tutorial

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
+ marsh
- https://realpython.com/flask-connexion-rest-api-part-2/
- https://towardsdev.com/create-a-rest-api-in-python-with-flask-and-sqlalchemy-e4839cd61ddd