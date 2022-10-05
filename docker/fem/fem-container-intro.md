# [Complete Intro to Containers (feat. Docker)](https://frontendmasters.com/courses/complete-intro-containers/)

- [site](https://btholt.github.io/complete-intro-to-containers/)
- [setup](https://github.com/btholt/complete-intro-to-containers/blob/master/README.md)

## Historical

- Bare metal = your code running on the bare metal
- Virtual machine: pick OS, thinks it's the only OS though many VMs can install on one bare metal
- Cloud services

## Crafting Containers By Hand

- **chroot**: linux command to set the root directory of new process limiting the new process to see outside of it
  - `chroot /my-new-root bash`
  - called "jail", cannot see out of current dir
- P: from this new process we can see and kill other processes
- **namespaces**: allow us to hide processes from other processes
  - `unshare` creates a new isolated namespace from its parent (so you, the server provider can't spy on Bob nor Alice either) and all other future tenants
- P: each isolated environment still has access to all physical resources of the server
- **cgroup**: control group, to limit CPU / memory to isolated environments

## Docker

- docker hub = npm for containers
- Image: pre-made container, made via dumping out the state of the container packaging it up and storing it to use later
- `docker run --interactive --tty alpine:3.10 # drop you in as root`
- `docker run ubuntu:bionic ls # ls = command to run, post ls this will shutdown`
- `docker run -dit ubuntu:bionic # runs in background`
- `docker ps # print all running containers`
- `docker attach <ID or name>`

- Run in background with name, kill(stop), remove

  - `docker run -dit --name my-ubuntu ubuntu:bionic` - `docker kill my-ubuntu`
  - `docker rm my-ubuntu`

- Auto remove when killed

  - `docker run --rm -dit --name my-ubuntu ubuntu:bionic`
  - `docker kill my-ubuntu`

- Node
  - `docker run -it node:12-stretch`
  - Without :12-stretch, default is latest tag
- **Alpine linux**: very tiny distro of linux (as opposed to ubuntu and debian)

## [Docker CLI](https://btholt.github.io/complete-intro-to-containers/docker-cli)

- `docker pull jturpin/hollywood # pre-fetch container to run`
- `docker inspect node # show info about container`
- `docker pause <ID or name>`
- `docker unpause <ID or name>`
- `docker exec <ID or name> ps aux # see it output all the running processes of the container`
  - Execs a command against already running container, whereas run is running a new container

## Node app

[See simple-node](./simple-node/index.js)

- `docker build -t my-node-app:1 .`
  - -t = --tag
- `docker run my-node-app:1`
- `docker run --init -p 3000:3000 my-node-app:1`
  - -p = --publish, port forwarding
  - --init tells docker to handle shutdown on control+c

## Layers

```Dockerfile
FROM node:12-alpine
USER node
RUN mkdir /home/node/code
WORKDIR /home/node/code
COPY --chown=node:node . .
RUN npm ci
CMD ["node", "index.js"]
```

- [Docker layers](https://dzone.com/articles/docker-layers-explained)
- for every rebuild we copy then npm install
- the cache will be not be used given index.js changes
- but why not reuse the cache?

```Dockerfile
FROM node:12-alpine
USER node
RUN mkdir /home/node/code
WORKDIR /home/node/code
COPY --chown=node:node package-lock.json package.json ./
# ./ means put in the directory
RUN npm ci

# above cache layer will be used if no changes to package-lock, then build picks up from src code changes
COPY --chown=node:node . .
CMD ["node", "index.js"]
```

## Making your own alpine node container

- see [custom-alpine-node.Dockerfile](./custom-alpine-node.Dockerfile)

## Static assets project / Multi-stage builds

- Create the react app
  - `npx --ignore-existing create-react-app static-assets-project --template typescript --use-npm`
  - If ignore existing doesn't work...
  - `npm uninstall -g create-react-app`
  - `npx clear-npx-cache`
  - `npx create-react-app static-assets-project --template typescript --use-npm`
- Build the react app
- From the container serve the built static assets

## "Stateful" containers

### Bind mounts

- **Bind mounts**: allow you expose files from your host computer into your container
- `docker run --mount type=bind,source="$(pwd)"/build,target=/usr/share/nginx/html -p 8080:80 nginx:1.17`
  - run from the root directory of your CRA app as we will serve the local build files inside from a nginx container, no other dockerfile needed. For dev environments
  - type can be bind / volume / other (tmpfs for secrets)
  - source = identify what part of the host we want to make readable-and-writable to the container. It has to be an absolute path (e.g we can't say "./build") which is why use the "$(pwd)"
  - target is where we want those files to be mounted in the container. Here we're putting it in the spot that NGINX is expecting.

### Volumes

- **Volume**: also persistent, but managed by docker. For databases / logs
- see volumes folder

## [Containers for dev environment](https://btholt.github.io/complete-intro-to-containers/visual-studio-code)

- See complex-node
- folder must be .devcontainer
- Open just the root folder with Vscode
- Extensions and settings auto installed

## [Networking with Docker](https://btholt.github.io/complete-intro-to-containers/networking)

- `docker network ls`

### Allow 2 mongo containers to talk to each other

- `docker network create --driver=bridge app-net # app-net name`
  - create new network
- `docker run -d --network=app-net -p 27017:27017 --name=db --rm mongo:3`
  - creates a mongo server
- `docker run -it --network=app-net --rm mongo:3 mongo --host db `
  - creates mongo client (that can connect to the database)
  - db here matches the `--name=db`

### Connecting our Node.js App to MongoDB

- see networking folder, builds off of above "2 mongo containers"

## Docker compose

- useful for dev environments / CI, less so for prod
- **Docker compose**: one dockerfile for many containers
- [see networking/docker-compose](./networking/docker-compose.yml)

## [Kubernetes](https://btholt.github.io/complete-intro-to-containers/kubernetes)

- **Master**: server that coordinates everything else, brain of the cluster
- **Nodes**: worker servers that are actually going to be running your containers. One node can one or multiple containers. Destination for containers
- **Pod**: an atom to a cluster: it's a thing that can't be divided and thus needs to be deployed together. Imagine if you had several types of containers that all worked together as one unit and wouldn't work without each other. In this case, you'd put those into a pod. Ex. The MongoDB and app are separate pods because they can scale individually.
- **Service**: a group of pods that make up one backend. Pods are scaling up and down all the time and thus it's unreliable to rely on a single pod's IP. Hence we need a service, a reliable entry point so that these services can talk to each other independent of the relative scale of each other. Services can be more than a backend, they can machine learning nodes, database, caches, etc.
- **Deployment**: is where you describe what you want the state of your pods to be and then Kubernetes works to get your cluster into that state.

### Installation

- [install kubectl](https://kubernetes.io/docs/tasks/tools/) for controlled k8s clusters
- kubectl is the same tool to control prod deployment, see [getting started on AWS EKS](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html)
- enable Kubernetes on Docker Desktop, open the preferences of Docker Desktop, navigate to the Kubernetes tab, enable it, alt is [minikube](https://minikube.sigs.k8s.io/docs/start/)

## [Kompose](https://btholt.github.io/complete-intro-to-containers/kompose)

- **Kompose**: converts a docker-compose.yml to a kubernetes configuration
  - [installation](https://kompose.io/installation/)
- `kubectl proxy --port=8080`
- `kubectl get all`
- `kubectl scale --replicas=5 deployment/web`
- `kubectl delete all --all`
- `kompose convert`
