DROP TABLE IF EXISTS url_data;

-- https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-serial/
CREATE TABLE url_data (
  id SERIAL PRIMARY KEY,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  long_url varchar (150) NOT NULL
);