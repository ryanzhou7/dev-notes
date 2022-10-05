## Intro

This guide teaches DevOps through the development and scaling of a [TinyUrl](https://tinyurl.com/app) clone. We will build the MVP, see the problems that we run into, then make necessary code and infrastructure changes needed. At the finale, the app should be able to scale to millions of users and you should be able to understand [system design diagrams](https://github.com/donnemartin/system-design-primer) with ease. It is much easier to learn DevOps after understanding the basics of backend development. Hence we begin with...

  <br/>

## Backend development with flask

- Read just enough of the [flask tutorial](https://flask.palletsprojects.com/en/2.2.x/tutorial/) such that you can create the tiny URL app. Which has these features

Functional requirements

- [ ] GET endpoint that shows the user a page where he can enter an url to shorten
- [ ] POST endpoint to save the url the user entered and returns a page that shows the shortened URL
- [ ] GET endpoint where given the short url, the browser will be redirected to the long URL

Non functional requirements

- [ ] Store the urls in an Sqlite database

Other notes

- Security is not a concern in the prototype. Security, although important, will not be the focus of these guide. There will only be as much security as needed to get through the guide. Do shutdown your cloud resources though.

<br/>

## Deploy prerequisites

Now we'd like to deploy our application on AWS

- [ ] Bookmark this [open source guide](https://github.com/open-guides/og-aws) and [AWS in English](https://expeditedsecurity.com/aws-in-plain-english/) for reference as needed
- [ ] Create an AWS account
- [ ] Read [creating an EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html) but DO NOT create one yet
- [ ] Note the different AMI of the EC2 creation step
- Now we use docker to get a local "practice server"
- [ ] [Setup docker desktop](https://www.docker.com/get-started/)
- [Optionally - read a docker crash course guide](https://blog.gruntwork.io/a-crash-course-on-docker-34073b9e1833)
- [ ] Pull an AmazonLinux docker image and run it locally
- [ ] Install python3 in the container (of the Amazon Linux)
- [ ] Copy the flask code into the container
- [ ] Run the app in the container, expose a port so your local browser can access the app
- [ ] Write all of the commands needed run the app in the container in `run.sh` script
- You are now ready to do this on an EC2 instance

<br/>

## EC2

Ready for EC2 usage

- [ ] Login into AWS and setup some billing alarms
- [ ] Read about [SSH and SCP](https://acloudguru.com/blog/engineering/ssh-and-scp-howto-tips-tricks)
- [ ] [Create your EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html), choose AmazonLinux
- [Alternative resource to creating EC2 instance](https://blog.gruntwork.io/a-crash-course-on-aws-59e4bc0bf398)
- [ ] SSH into that EC2 from your local and note that it is the same as the docker container we started
- [ ] SCP your code into your EC2 instance
- [ ] Run the `run.sh` script
- [ ] `curl localhost:5000` to test that is is working locally to this server
- [ ] Test from the public endpoint so that you can access the app

<br/>

## Terraform

We have deployed our app but it is not best practices. The solution to this "ClickOps", (clicking to create the ec2)? Terraform, aka IAC. We want to learn just enough TF to be able to do the same deployment we did above.

- [ ] [Read about ClickOps](https://www.lastweekinaws.com/blog/clickops/)
- [Optionally - read a TF crash course guide](https://blog.gruntwork.io/a-crash-course-on-terraform-5add0d9ef9b4)
- [ ] [Do some of the terraform CLI tutorials](https://developer.hashicorp.com/terraform/tutorials/cli) just enough to understand the next
- [ ] [Do all of the TF AWS tutorials](https://developer.hashicorp.com/terraform/tutorials/aws-get-started)

<br/>

## Terraform + AWS IRL

Now we'd like to use terraform in our AWS account, but theres some prework before we can do that.

- [ ] [Click an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)
- [ ] See that you can now login into this IAM user
- [ ] [Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- [ ] Login into AWS CLI with your new IAM user
- [ ] Create a EC2 instance via TF
- [ ] Deploy to that instance to ensure that it is the same as the server your initially created
- [ ] Apply a terraform change to this EC2 instance that upgrades the server's specs
  - This is a form of vertical scaling, this is needed as you need faster compute speed

<br/>

## Horizontal scaling

Great news, the app is doing great. There are 100s of users and growing. We've tried to resolve this by upgrade the server repeatedly, but at some point it is simply not possible or cost efficient. What we need to do instead is some horizontal scaling

- [ ] [Read about horizontal scaling](https://www.stormit.cloud/blog/scalability-in-cloud-computing-horizontal-vs-vertical-scaling/)
- [ ] Realize that you need a load balancer and [create one](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html)
- You might need to read up on networking concepts
- Optionally do this in TF
- [ ] Ensure that your load balancer now resolves to 2 ec2s

<br/>

## Database upgrade

That was great! However, now there's a bug. Each of the servers uses their own Sqlite database, which means that if an user creates an url, there's a ~50% chance that the url wouldn't found. Plus, how do we make the database faster when that becomes the bottleneck? One answer us using a Postgresql database.

- [ ] Use docker to start up a Postgresql database locally
- [ ] Download [pg admin](https://www.pgadmin.org/) or install Vscode extension that lets you connect to that database
- [ ] Run the SQL on the postgresql database to get the same schema
  - You might have to modify the sql as postgres and Sqlite might have [slight dialect differences](https://www.datacamp.com/blog/sql-server-postgresql-mysql-whats-the-difference-where-do-i-start)
- [ ] Configure the backend app to use the local postgresql database
  - [Resource by Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-use-a-postgresql-database-in-a-flask-application)
  - [Resource by Real Python](https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/)
  - [Resource by Towards data-science](https://towardsdatascience.com/sending-data-from-a-flask-app-to-postgresql-database-889304964bf2)
- [ ] Partially follow [this guide](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/TUT_WebAppWithRDS.html) and create an postgres RDS instance that is publicly accessible
- [ ] Confirm public accessibility by connect to the postgres RDS from your local client (pg admin or Vscode extension)
- Optionally create the postgres RDS in TF
- [ ] Connect your local backend app to the postgres RDS
- [ ] Redeploy your local backend such that it connects to the postgres RDS from the EC2 it is hosted on

<br/>

## Choose your adventure, DevOps or Frontend

By default this guide will now continue to the "Modern DevOps", that is dockerizing the backend / using ECR then using kubernetes / EKS. However, you may take a "Frontend scaling" detour which will entail using AWS S3, AWS Cloudfront, Github actions, and making some necessary flask app changes.

<br/>

## Modern DevOps - Dockerizing with ECR

- [ ] Read about [the benefits of using docker](https://dzone.com/articles/top-10-benefits-of-using-docker)
- [ ] Dockerize the backend application, i.e. create an image with this code
  - [Resource](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xix-deployment-on-docker-containers)
- [ ] [Create a public AWS ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-cli.html)
- [ ] Push your docker image to the AWS ECR you created
- Optionally create the ECR in TF
- [ ] Pull your docker image from AWS ECR and confirm that it runs locally
- Optionally run your image in ECS, very "optional" as this is not used as often

<br/>

## Kubernetes

- Optional read [crash course on kubernetes](https://blog.gruntwork.io/a-crash-course-on-kubernetes-a96c3891ad82)
- [ ] Turn on k8 in Docker desktop
- [ ] Install [kubectl](https://kubernetes.io/docs/reference/kubectl/)
- [ ] Create a kubernetes cluster with multiple backends locally
- [ ] Create a kubernetes cluster with multiple backends + the postgres database locally
- [ ] [Read about AWS EKS](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html)
- [ ] [Use TF to deploy a k8 cluster](https://blog.gruntwork.io/a-crash-course-on-terraform-5add0d9ef9b4) then be ready to shut it down quickly, BEWARE EKS is expensive
- [ ] Note the that EC2 instances are started with EKS, EKS deploys to EC2 instances

Congratulations! You have graduated!

<br/>

## Frontend scaling - detour / bonus

Now we have to decouple the front and backend. Application changes

- [ ] [Set up a react/ts repo with vite](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-react-project-with-vite)
- [ ] Replicate the flask frontend in react
- [ ] Change the backend routes such that it returns a non-200 status code if an url was not found
- [ ] Run the frontend and backend locally, see that it works
- [ ] Try to hit one of the deployed backends and see that you might need [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/)

<br/>

## Frontend deploy

- [ ] Build the react locally
- [ ] [Host this website in AWS S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html)
- Optionally do this in TF
- [ ] Build the react such that it hits the deployed backend and ensure it works
- [ ] [Create a cloud front distributes from site in S3](https://aws.amazon.com/blogs/networking-and-content-delivery/amazon-s3-amazon-cloudfront-a-match-made-in-the-cloud/)
  - See next checkbox for additonal resource
- [ ] [Create a GitHub Action that](https://frontendmasters.com/courses/aws-v2/)
  - [ ] Builds react
  - [ ] Deploys to S3
  - [ ] Invalidates the cloud front distributions

You're all done!!!

<br/>

## AWS Lambda Bonus

- [ ] [Getting started](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html)

<br/>

## AWS Networking bonus

- [ ] [AWS Ramp-Up Guide: networking and content delivery](https://d1.awsstatic.com/training-and-certification/ramp-up_guides/Ramp-Up_Guide_Networking-Content-Delivery.pdf)

<br/>

## Flask bonuses

- [ ] [Async flask 2.0](https://testdriven.io/blog/flask-async/)
- [ ] [Flask migrate - alembic](https://github.com/miguelgrinberg/Flask-Migrate)
- [ ] [Awesome flask - huma](https://github.com/humiaozuzu/awesome-flask)
- [ ] [Awesome flask - mjhea](https://github.com/mjhea0/awesome-flask)

<br/>

## SQS bonus

- [ ] [Mange queues and messages](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.html)

<br/>

## Cloud native landscape

- [ ] [CNCF Cloud Native Interactive Landscape](https://landscape.cncf.io/)
