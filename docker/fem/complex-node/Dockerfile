# docker build -t my-node-app:2 .
# docker run --init -p 3000:3000 my-node-app:2

FROM node:12-stretch

USER node 
RUN mkdir /home/node/code
# need as now user owns this dir

WORKDIR /home/node/code

COPY --chown=node:node . .
RUN npm ci 
# npm ci adheres to package-lock and faster than npm i

CMD ["npm", "run", "start"]
# should only be in CMD per file