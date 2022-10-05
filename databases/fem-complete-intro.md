# [Complete Intro to Databases](https://btholt.github.io/complete-intro-to-databases/)

## Intro

- **query**: command sent to a db to get it to do something
- **schema**: rigid structure used to model data

### Database types not covered

- **Search engines**: like Solr or Sphinx are often paired with databases to make search possible. If your database doesn't support full-text search this is a tool you could pair with a database to make a site-wide search engine possible.
- **Wide Column Databases**: uses the concepts of tables, rows, and columns like a relational database but has a dynamic nature to those formats of rows and names. As such it can sorta be interepted like a two dimensional key-value store. Apache Cassandra and Google Bigtable are two famous examples of this. These databases are famous for being able to be massive scale and very resilient.
- **Message brokers**: are a vastly underutilized piece of architecture by Node.js developers that can really improve your flexibility and scalability without greatly increasing complexity. They allow apps and services to publish events/messages on a system and allow the message broker to publish/inform subscribers to those events that something happened. It's a powerful paradigm. Apache Kafka, RabbitMQ, and Celery are all related to this paradigm.
- **Multi model databases**: are databases that can actually operate in multiple different ways, fulfilling more than one of these paradigms. Azure Cosmos DB and ArangoDB are two primary examples of this. MongoDB and PostgreSQL technically are these as well since they have features that allow you to bend them into different shapes.

### ACID: atomicity, consistency, isolation, durability

- key factors one should think about when thinking about writing queries.
- **Atomicity**: Are transactions all or nothing? Ex. a query to transfer $1 from account A to account B, if a failure occurred at step 2 but not 1 then $10 was lost in totality
- **Consistency**: "any change maintains data integrity or is cancelled completely", ex. setting number to a boolean column
- **Isolation**: a query that is doing many things can be run serially or in parallel (same result for running it either way)
  - Virtually all dbs are this now
- **Durability**: "changes made to the database (transactions) that are successfully committed will survive permanently, even in the case of system failures", i.e. your data remains even if the server crashes

- **Transaction**: an atomic multi-query, important when multi queries are needed accomplish the thing

<br/>

## [NoSQL](https://btholt.github.io/complete-intro-to-databases/nosql)

- **NoSQL**: not a relational db
- Focus on document based db (mongodb)
- document based db means you don't need to define shape of data (Ex. sql, column will be int)

- Run mongodb
  - `docker run --name test-mongo -dit -p 27017:27017 --rm mongo:4.4.1`
  - `docker exec -it test-mongo mongo # start container named mtestmongo and run mongo cmd`
- **database in mongo**: group of collections
- **Collection**: groups of documents, can have capabilities (store 10 docs here at most and discard oldest when getting the 11th doc)
- `use adoption # use the adoption db or create it if it dne`
- document = record = entry in collection
- `db.pets.insertOne({name:'Luna', type:'dog'}) # in pets collection insert`
  - id auto created by mongo and returned
- `db.pets.help # show all commands or 'db.help()'`
- `db.pets.findOne({name: 'Luna'});`
- `db.pets.find({name: 'Luna'}); # return iterator`
- `db.pets.find({name: 'Luna'}).toArray(); # returns all`

### [Querying mongo db](https://btholt.github.io/complete-intro-to-databases/querying-mongodb)

- **projection**: returning just some fields of the data is is found
- [updating mongo db](https://btholt.github.io/complete-intro-to-databases/updating-mongodb)
- **upsert**: insert a new document with these things if you don't find one that exists with that
- findAnd\* : findOneAndUpdate, find and do something
- bulkWrite: give array of queries

### [Indexes](https://btholt.github.io/complete-intro-to-databases/indexes-in-mongodb)

- `db.pets.find({type: 'dog'}).explain('executionStats')`
  - COLLSCAN: worst case, look at every document in the collection
- **index**: data structure in database for quick lookup, can cause inserts, updates, and deletes to be slower as the index needs to be also updated
- `db.pets.createIndex({type: 1})`
  - now the execution stats should show FETCH
- `db.pets.getIndexes()`
- `db.pets.createIndex({index: 1}, {unique: true}) // create unique index`
- Text index
  - `db.pets.createIndex({ type: "text", breed: "text", name: "text", });`
  - `db.pets .find({ $text: { $search: "dog Havanese Luna" } }) .sort({ score: { $meta: "textScore" } });`
  - Each collection can only have one text index

### [Aggregation](https://btholt.github.io/complete-intro-to-databases/aggregation)

- See how many puppies, adult, and senior dogs we have in our pets collection?
  - `db.pets.aggregate([ { $bucket: { groupBy: "$age", boundaries: [0, 3, 9, 15], default: "very senior", output: { count: { $sum: 1 }, }, }, }, ]);`
  - `{ "_id" : 0, "count" : 1112 }`
  - `{ "_id" : 3, "count" : 3336 }`
  - `{ "_id" : 9, "count" : 3332 }`
  - `{ "_id" : "very senior", "count" : 2221 }`
- Aggregation can be done via stages, ex. match, bucket, sort

### [Node.js app with MongoDB](https://btholt.github.io/complete-intro-to-databases/nodejs-app-with-mongodb)

### [MongoDB Ops](https://btholt.github.io/complete-intro-to-databases/mongodb-ops)

- **Replica set**: set of MongoDB servers (all running the mongod process) that all have the same set of data on them. (if one of the servers goes down, there are other servers available to step up and continue running without downtime as well as making sure that if a server blows up that you're not losing data)
- **Primary server**: the server that can accept reads (queries that don't modify anything e.g. find) and writes (queries that do modify things e.g. deleteOne, insertMany, etc.)
- **Secondary servers**: can only accept reads. All writes must go through the primary. MongoDB has eventual consistency
- **Eventual consistency**: That means the secondaries may have a lag time between when you write to the primary and when it updates the secondary. MongoDB does have the ability to set write priorities so you can make your app pause until it can guarantee that all secondaries have received the write. This breaks the Consistency in ACID
- **Arbiters**: a "thing" that only votes in the **elections** (doesn't store data) which secondary should become the primary in case of failure
- **Managed Cloud Version**: services that manage all of the above, ex. MongoDB Atlas, Microsoft Azure Cosmos DB, or Amazon Web Services DocumentDB

<br/>

## [SQL](https://btholt.github.io/complete-intro-to-databases/intro-to-sql-databases)

- SQL = relational = structured schema = cannot create on the fly
- SQL: can join tables (that relate to each other)
- NoSQL: don't join documents across collections

### Landscape

- MySQL: owned by Oracle, mature
- MariaDB: fork by original MySQL creators
- SQLite: meant to live on the app server
- Microsoft SQL Server / Oracle / DB2: commercial products, expensive
- PostgreSQL: Open source continues to gain market share

### [PostgreSQL](https://btholt.github.io/complete-intro-to-databases/postgresql)

- Db creation
  - `docker run --name my-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d --rm postgres:13.0`
  - `docker exec -it -u postgres my-postgres psql`
  - `CREATE DATABASE message_boards;`
    - All caps conventions
  - `\c message_boards;`
    - connect o this database
  - `\d` : see all tables in this db
  - `\h` : show all queries
  - `\?` : see all commands

```sql
CREATE TABLE users (
  user_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY, -- auto increment. PK is auto indexed
  username VARCHAR ( 25 ) UNIQUE NOT NULL, -- VARCHARS = string
  email VARCHAR ( 50 ) UNIQUE NOT NULL,
  full_name VARCHAR ( 100 ) NOT NULL,
  last_login TIMESTAMP,
  created_on TIMESTAMP NOT NULL
);
```

- [All postgresql data types](https://www.postgresql.org/docs/9.5/datatype.html#DATATYPE-TABLE)
- `INSERT INTO users (username, email, full_name, created_on) VALUES ('btholt', 'lol@example.com', 'Brian Holt', NOW());`
- `select * from users;`
- [Mock data to copy and paste](https://btholt.github.io/complete-intro-to-databases/sample-postgresql.sql)
- Querying basic to complex
  - `SELECT username, user_id FROM users LIMIT 15; -- projection`
  - `SELECT username, email, user_id FROM users WHERE user_id=150;`
  - `SELECT username, email, user_id, created_on FROM users WHERE last_login IS NULL AND created_on < NOW() - interval '6 months' LIMIT 10;`
    - Users that haven't logged in and created 6+ months ago
  - `SELECT user_id, email, created_on FROM users ORDER BY created_on DESC LIMIT 10;`
  - `UPDATE users SET last_login = NOW() WHERE user_id = 1 RETURNING *;`
    - returning \* optioanal
  - `UPDATE users SET full_name= 'Brian Holt', email = 'lol@example.com' WHERE user_id = 2 RETURNING *;`
    - Must use single quotes
- [Foreign keys](https://btholt.github.io/complete-intro-to-databases/complex-sql-queries#foreign-keys)
- [Query complex](https://btholt.github.io/complete-intro-to-databases/complex-sql-queries)
- [Storing JSON](https://btholt.github.io/complete-intro-to-databases/json-in-postgresql)
- [Indexes](https://btholt.github.io/complete-intro-to-databases/postgresql-indexes)
- [Sample app](https://btholt.github.io/complete-intro-to-databases/nodejs-app-with-postgresql)

### [Hasura](https://btholt.github.io/complete-intro-to-databases/hasura)

- **Hasura**: server you will put inside your cluster of servers that allows you to treat your database like it was a GraphQL data source

### [PostgreSQL Ops](https://btholt.github.io/complete-intro-to-databases/postgresql-ops)

<br/>

## [Graph databases](https://btholt.github.io/complete-intro-to-databases/graph-databases)

- **Node**: a thing
- **Label**: goes on a node to denote what kind of node this is
- **Relationships / Edges **: direction connection between nodes
- **Properties**: can exist on both nodes and relationships, like fields / columns

### [Neo4j](https://btholt.github.io/complete-intro-to-databases/neo4j)

- **Cypher**: query language of Neo4j
- `docker exec -it my-neo4j cypher-shell`
- `CREATE (Person {name:'Michael Cera', born:1988});`
  - Create node with Person label and props
- `MATCH (p {name: "Michael Cera"}) RETURN p;`
  - p is a variable, can be anything
- `MATCH (p: Person) RETURN p;`
  - matches all persons
- `CREATE (m: Movie {title: "Scott Pilgrim vs the World", released: 2010, tagline: "An epic of epic epicness."}) return m;`
- `MATCH (p) RETURN p;`
  - get all nodes
- creating a relationship Michael and movie
  - ACTED_IN screaming case is convention
  - note the -> directional

```
MATCH (Michael:Person),(ScottVsWorld:Movie)
WHERE Michael.name = "Michael Cera" AND ScottVsWorld.title = "Scott Pilgrim vs the World"
CREATE (Michael)-[relationship:ACTED_IN {roles:["Scott Pilgrim"]}]->(ScottVsWorld)
RETURN relationship;
```

## [Key-value store](https://btholt.github.io/complete-intro-to-databases/key-value-store)
