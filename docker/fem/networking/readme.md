## Used the hapi ex again

- init and `npm install mongodb@3.3`
- `docker build -t app-with-mongo .`
- `docker run -p 3000:3000 --network=app-net --env MONGO_CONNECTION_STRING=mongodb://db:27017 app-with-mongo`
  - Connects to the container with mongo

## docker compose

- `docker-compose up`
- `docker-compose up --build # force rebuild`
- `docker-compose up --scale web=10`
  - starts 10 web containers, but won't work due to binding on the same port. Need Nginx
