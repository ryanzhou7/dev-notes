# Fullstack & DevOps

## Backend

- Run the flask app in /backend locally
- Note v1 of the code then return here

## Deploy prerequisite

### Intro

- We want to this app to be running on a server (a computer that is always on)
- We can rent one out from AWS, but what is AWS?
- AWS is a cloud services company (comparable to Azure, Google cloud platform, Digital Ocean)
- Cloud services company: write software, which you can use and have hardware, which you can rent
- The combination of software + hardware = services
- AWS has 100s of services, which can be categorized by [less a dozen categories](https://aws.amazon.com/products)
- The primary ones are compute, storage, database, networking & content delivery
- Compute aka run my code, which is what we want
- Click "Compute" in their [products](https://aws.amazon.com/products)
- We'll focus on [EC2, virtual servers in the cloud](https://aws.amazon.com/ec2/?did=ap_card&trk=ap_card) because we'd like to rent a server to run our code
- But first we need to create an account

### Account creation

- [Create and activate a AWS account](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/)
- AWS has a [generous 12 month free tier](https://aws.amazon.com/free/), of which you can repeatedly use with the "same" email address by utilizing the [+ trick](https://people.cs.rutgers.edu/~watrous/plus-signs-in-email-addresses.html)
- You will need a credit card, if we're careful it won't be charged
- After signing up go to the [https://console.aws.amazon.com/console/home](https://console.aws.amazon.com/console/home)
- Note that you will be auto redirected to a [region](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) ex. [https://us-west-1.console.aws.amazon.com/](https://us-west-1.console.aws.amazon.com/) denotes the US-WEST-1 region which is Northern california
- The links will reference us-west-1 from now on, unless stating another region specifically

### EC2

- [Guides like this](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html) teach you how to create a ec2 instance, follow it until you see where you pick your AMI i.e. [this page](https://us-west-1.console.aws.amazon.com/ec2/home?region=us-west-1#LaunchInstances:)
- AMI is a template that contains the software configuration (operating system, application server, and applications) required to launch your instance
- Before we create our ec2, lets see what it's like inside a AmazonLinux or Ubuntu OS computer

### AmazonLinux

- The best way to access this OS is through docker
- Download [Docker Desktop](https://www.docker.com/get-started/) and start it up
- If you open a terminal and type `docker --version` you should see something like `Docker version 20.10.17, build 100c701`
- There will be many of these command line inputs (what you type) / output(what is expected to be seen)
- These will be abbreviated like the following
- `docker --version`
  - `Docker version 20.10.17, build 100c701` or something similar
- The indent will always be a note, expected output or both
- There may not be an indent for every command
