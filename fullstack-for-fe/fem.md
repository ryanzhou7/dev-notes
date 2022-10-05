# [Full Stack for Front-End Engineers, v2](https://frontendmasters.com/courses/fullstack-v2/)

- [slides](https://docs.google.com/presentation/d/1Mvf_rOFz1wZeH1irajJqhRQgzid7BkqJBd8wigpz39M/edit#slide=id.p)

## Understanding the internet

- **Intranet**: private internet
- IP: internet protocol, agreed upon way to communicate
- **TCP**: transmission control protocol: lossless, has error checking (checksum)
- **UDP**: user datagram protocol: hey U, then assume you heard me. Faster than TCP (data blast)
- `traceroute google.com # DNS says IDK but he might know, pass to them`
- **VPS**: virtual private server, slice of a real server
- DNS records
  - A record: maps name to IP address
  - CNAME: maps name to name, ex. blog.jemyoung.com -> jemyoung.com
  - `dig blog.jemyoung.com # to see DNS records`

<br/>

## Server setup

- **Nginx**: reverse proxy, web server (serves static requests)
  - regular proxy: takes many requests and proxies to 1 place
  - reverse proxy: take 1 request and proxy somewhere else
- `apt install nginx && service nginx start # auto opens port 80`
  - this was done on the same server with the app running
- [Ex. config](http://nginx.org/en/docs/beginners_guide.html)
- Web server different from application server (node / express)
- domain -> IP -> Nginx (web server) -> express (app server) or static files
- `vim /etc/nginx/sites-available/default # config below`

```
  server {
      # auto forward http://ip :80 of server -> node :3000
      location / {
          proxy_pass http://localhost:3000/;
      }

      # filter all requests ending in .gif to /data/images directory
      location ~ \.(gif|jpg|png)$ {
          root /data/images;
      }
  }

```

- `service nginx reload # after above config change`
- **Service**: highest level command for daemon
- **Process manager**: keep app running, handles logging, errors, restarts
- `npm i -g pm2 && pm2 start node_app.js`
- `pm2 startup # setup auto start on server starts`
- `pm2 save # to save`
- `pm2 stop 0 # stop process 0`
- [express docs](https://expressjs.com/en/advanced/best-practice-performance.html) on how performance tune, including nginx config

<br/>

## Security

- **0 day vulnerability**: vulnerability that is disclosed but not patched
- `sudo apt install unattended-upgrades`
  - "The best thing you can do is keep software up to date"
- **Firewall**: perimeter security technique that allow/blocks requests depending rules
- `apt install nmap && nmap -sV SERVER_IP_ADDRESS`
  - shows what ports are open and what processes are running
- **Port**: Communication endpoint that maps to a specific process or network service
  - `less /etc/services # see standard ports`
- `iptables -p tcp --dport 80 -j REJECT`
  - A way of routing / denying requests over certain protocols
  - But `ufw` uncomplicated firewall is friendlier
- `ufx allow/deny/reject http/https/ssh`
  - permutations above with "/"
  - `ufw deny http` blocks ALL traffic to http standard port rather than saying block TCP, UDP, traffic etc...
  - deny: black-hole
  - reject: replies with response
  - `ufw status verbose`
- [Explain shell](https://explainshell.com/)

<br/>

## HTTP

- Request + response model
  - Header: metadata, "writing outside of the envelope", contains
    - Host: where the request is going
    - User-Agent: browser of the request
    - Accept: what can be requested from the server
    - Content-type: the type of media
    - Set-cookie: data that persists on the browser, set with every request
    - X-: custom headers
  - Response
    - Status code: indicates status of request
  - HTTPS: SSL / encryption over http so no one can inspect your http request. Also, to confirm the website is "real" (certificate authority)
  - [Cert bot](https://certbot.eff.org/) to auto mod nginx to https and add certificate
- **HTTP/1**: Every request is over TCP which needs a seperate long handshake (send syn, get back ack)
- **HTTP/2**: relies https in place, can multiplex: make one connection and stream everything over one pipe, and uses hpack compression algo [speed diff demo](https://http2.akamai.com/demo)
  - Edit `vi /etc/nginx/sites-available/default`
  - Add `listen 443 http2 ssl;`
- **HTTP/3**: Quick UDP internet connections (vs prev gen TCP for http:1/2)

<br/>

## Containers

- Benefits
  - Lightweight: only what it needs
  - Portable: deploy anywhere
  - Decouples app from infrastructure
- Containers exs: docker, AWS ECS, apache mesos
- **Orchestration**: - rolling out
  - exs: k8, docker swarm, AWS EKS, apache mesos, Azure AKS
- `top # see current proceses, q to quit`
- `htop # better`
- Nginx can be a load balancer
- Deployment exs: ansible, vagrant, puppet, chef (server setup)

<br/>

## Saving Data

- **relational db**: sql, tables, strict structure
- **non-relational db**: no-sql, data agnostic, loose structure
  - exs: redis (k/v store), elastic, mongodb (documents), cassandra
- **Websocket**: persistent bidirectional connection between client / server, (streaming data).
  - Previously, long polling = open TCP connection and keep alive via continuous data pushing
- build chat websocket exercise
  - change nginx to allow websocket
  - express app responds
  - [websocket app repo](https://github.com/young/fsfev2)
