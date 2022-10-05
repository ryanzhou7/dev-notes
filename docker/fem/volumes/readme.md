- `docker build --tag=incrementor .`

- Destroys the file between runs

  - `docker run incrementor`

- Persists with volumes

  - `docker run --env DATA_PATH=/data/num.txt --mount type=volume,src=incrementor-data,target=/data incrementor`
  - env flag to tell node app where to write file
  - "incrementor-data" volume name, can omit
  - repeat this command to see the returned incrementor

- `docker volume list`
- `docker volume prune # remove all`
-
