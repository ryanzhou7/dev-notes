# docker build -t my-node-app:1 .
# docker run --init -p 3000:3000 my-node-app:1

FROM node:12-alpine
USER node 
# switch from root to existing node user from node:12-stretch
# RUN useradd -ms /bin/bash new-user

WORKDIR /home/node/code
# WORKDIR creates dir if dne, like cd

COPY --chown=node:node index.js .
# --chown=node:node so node user owns that file
# use COPY for local files, ADD for unzip / downloading

CMD ["node", "index.js"]
# should only be in CMD per file