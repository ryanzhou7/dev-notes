## Creating a server

- Launch instance
  - server1
  - Ubuntu
  - t2
  - keypair1
    - RSA, .pem
  - Security
    - launch-wizard-1: security group name created (EC2 feature)
    - allow ssh, https, http, my IP
    - Turn on billing
- Ec2 -> instances
  - connect
    - SSH client
      - [chmod](https://quickref.me/chmod)
      - `chmod 400 keypair1.pem`
      - `ssh -i "keypair1.pem" ubuntu@ec2-52-53-163-28.us-west-1.compute.amazonaws.com`

## [Configure IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)

- Users -> add user
  - username: user1
  - Programmatic, console, no reset
  - Attach existing policy:
    - AdminAccess
    - Administrator: gateway, audit, DB, network, system,
    - Billing: conductor billing all,+ billing
    - Max 10
  - tag: user1
    - Got access key ID + secret
  - default region: None
- user1
  - Security credentials
  - [sign in link](https://373281753717.signin.aws.amazon.com/console)

## AWS CLI install & login

- [Instructions](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
  - Command line installer all -users
  - `curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg" && sudo installer -pkg AWSCLIV2.pkg -target /`
  - `aws --version`
  - `aws configure`
    - Login with access key ID + secret from IAM

<br/>

## Creating a ECR registry

- Amazon ECR: Container registry
  - Private
    - name: ecr1
    - tag immutability: disabled
    - scan on push: disabled
    - KMS: disabled
    - View push commands via docker
  - Public
    - name: ecr2
    - OS: linux
    - x86-64
    - View push commands via docker

## Using ECR registry

- [Setting up with Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/get-set-up-for-amazon-ecr.html)
- [Using Amazon ECR with the AWS CLI](https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-cli.html)
  - Step 1 - build an image
    - `docker build -t hello-world1 .`
      - repository is hello-world1, Dockerfile in curr directory
    - `docker images --filter reference=hello-world1`
    - `docker run -t -i -p 80:80 hello-world1`
    - curl localhost:0080
  - Step 2 - push to ecr
    - `aws configure`
      - assume
    - View push commands - ecr
    - `aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/e4n8r4t5`
    - `docker build -t ecr2 .`
      - repository is ecr2
    - `docker tag ecr2:latest public.ecr.aws/e4n8r4t5/ecr2:latest`
      - tag so it can be pushed to repo
    - `docker push public.ecr.aws/e4n8r4t5/ecr2:latest`
      - push
  - Step 3 - pull image
    - `docker pull aws_account_id.dkr.ecr.region.amazonaws.com/hello-repository:latest`
      - Copy from URI, but this is private
      - region see ecr push commands
    - [Pulling an image from the Amazon ECR Public Gallery](https://docs.aws.amazon.com/AmazonECR/latest/public/docker-pull-ecr-image.html)
    - [Pulling an images](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-pull-ecr-image.html)
      - `aws ecr describe-repositories``
    - From amazon ECR -> repo -> ecr2
    - `docker pull public.ecr.aws/e4n8r4t5/ecr2:latest`
    - `docker run -t -i -p 80:80 public.ecr.aws/e4n8r4t5/ecr2`

## [ECS using Fargate](https://us-west-1.console.aws.amazon.com/ecs/home?region=us-west-1#/firstRun)

- highly scalable and fast container management service. You can use it to run, stop, and manage containers on a cluster
- Fargate: serverless infra that AWS manages
- [ECS vs EKS](https://platform9.com/blog/fargate-vs-upstream-kubernetes/)

## [Getting started with EKS](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html)

- [Install kubectl](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html)
- [Getting started](https://docs.aws.amazon.com/eks/latest/userguide/getting-started-console.html)
  - Creating your cluster
  - TBD

## [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/GettingStarted.html)

- [Quick start terraform](https://aws.amazon.com/quickstart/?solutions-all.sort-by=item.additionalFields.sortDate&solutions-all.sort-order=desc&awsf.filter-content-type=*all&awsf.filter-tech-category=*all&awsf.filter-industry=*all&solutions-all.q=terraform&solutions-all.q_operator=AND)
- [Github](https://github.com/aws-ia)
  - [Examples](https://aws-ia.github.io/terraform-aws-eks-blueprints/main/)
  - [Getting started](https://aws-ia.github.io/terraform-aws-eks-blueprints/getting-started/)
