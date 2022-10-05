- [Client-server model](https://cio-wiki.org/wiki/Client_Server_Architecture)
  > Client-server architecture is an architecture of a computer network in which many clients (remote processors) request and receive service from a centralized server (host computer). Client computers provide an interface to allow a computer user to request services of the server and to display the results the server returns. Servers wait for requests to arrive from clients and then respond to them.
- Backend app
  - index.js
  - deploy
- Linux intro
  - [OS history](https://btholt.github.io/complete-intro-to-linux-and-the-cli/static/17bba82d8a4f4795b3c8f7283a0a15ea/c2d13/linux_timeline.png)
  - Linus "created Linux because at the time there was no single free, open-source reimplementation of the Unix operating system"
  - "Linux isn't directly Unix, just directly inspired by it, and incorporates many of its ideas and interfaces into it."
  - **Linux distribution** = distro = something built with the [linux kernel](https://btholt.github.io/complete-intro-to-linux-and-the-cli/static/0bf2e8afad14f2735c1e049ab58f7c74/2bef9/linux_kernel_map.png)
  - **Ubuntu**: [downstream distro of Debian where downstream means that Ubuntu builds upon the base of Debian](https://cognitivewaves.wordpress.com/linux-distributions/)
  - **Shell**: "is a program that takes commands from the keyboard and gives them to the operating system to perform. In the old days, it was the only user interface available on a Unix-like system such as Linux, [source](https://linuxcommand.org/lc3_lts0010.php)
  - "Bourne Again SHell, an enhanced version of the original Unix shell program, sh, written by Steve Bourne"
  - **Terminal**: emulator that the shell runs inside. Ex. Terminal.app, iTerm2. Yyou can use that emulator to switch out what shell is running inside of it. For now we want to be on bash (or zsh is basically the same too.)
  - REPL - Read Evaluate Print Loop, like `$ python3` or `$ node`
- Server
  - Linux
  - [How To Use SSH to Connect to a Remote Server](https://www.digitalocean.com/community/tutorials/how-to-use-ssh-to-connect-to-a-remote-server)
  - [How to connect to AWS ec2 instance from Ubuntu terminal](https://www.how2shout.com/linux/how-to-connect-to-aws-ec2-instance-from-ubuntu/)
  - `chmod +x index.js`
- Backend app

  - https://github.com/nvm-sh/nvm
  - => Appending nvm source string to /home/ubuntu/.bashrc
    => Appending bash_completion source string to /home/ubuntu/.bashrc
    => Close and reopen your terminal to start using nvm or run the following to use it now:
  - locally
  - deploy

- Linux preq (skippable)

  - multi user, root, sudo
  - permissions
  - /bin

- Historical compute
  - bare metal
  - ec2, cloud service, pred vm
- Crafting docker (skippable)
  - change root: file isolation
  - namespace: process, network isolation
  - cgroups: process cpu, etc. limitation
- Docker p 1

  - `sudo apt install nodejs`
  - `chmod +x index.js`
  - Desktop / Hub / CLI
  - images
  - node container
  - tags
  - cli
  - dockerfile
  - node js app
  - ports & expose

- Databases

  - what
  - docker PostgreSQL
  - schema
  - query
  - app
  - AWS RDS

- Docker p2

  - layers
  - alpine node
  - multi stage builds
  - static assets
  - bind mounts
  - volumes
  - docker for dev env
  - networking
  - docker compose
  - kubernetes
  - kompose

- Http 1->2, Internet

  - A bunch of connected cables through which data can be transferred
  - IP: internet protocol, agreed upon way to communicate
  - client / server - request / response model

- Resources

  - intro linux
  - intro containers
  - fullstack for fe
  - databases
  - AWS knowledge

- [DevOps](https://roadmap.sh/devops)
  - OS concepts
  - networking
  - CI/code
  - infrastructure provision
