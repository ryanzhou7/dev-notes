DROP TABLE IF EXISTS url_data;

CREATE TABLE url_data (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  long TEXT NOT NULL
);