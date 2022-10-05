# Terraform: Up and Running

## Why Terraform

Cons of dev vs ops...

- Before: all infrastructure configured by hand, now: TF

### IAC tools

- Ad hoc scripts, CM tools, server templating, orchestration, provisioning

- **Configuration management tool**: install and manage software on existing servers, ex. chef, puppet, ansible
- **Idempotent code**: code that works correctly no matter how many times it is run
- **Server templating tools**: ex. docker, packer, vagrant. Create image of server that is the full container snapshot of the OS
  - Image tools
    - VM: drawback = CPU usage, memory usage, startup time
    - Container: no overhead
- You could use packer to create image of server then use ansible to install that image across all servers
- **immutable infrastructure**: if changes need to occur, change the IAC then deploy on new server
- **Orchestration tools**: ex. kubernetes, mesos, ECS
  - Orch tool tasks, deploy, auto heal, load balance, scale, allow containers to talk to each other (service discovery)
- **Provisioning tools**: creating infrastructure, i.e. servers, load balancers, queues, etc...

## Describe TF

- TF works via binary makes API calls on your behalf to providers
- TF:
  - Declarative style, rather than procedural
  - Domain specific language rather than general purpose
    - Ex. TF is HCL, Chef uses Ruby
  - Masterless vs have to run master server
  - Agentless vs agent
- Might need multiple tools, ex. TF + ansible, TF + packer, TF + docker + k8s

<br/>

## Getting started with TF

1. AWS sign up, create account, install TF, export credentials

```go
provider "aws"{
  region = "us-east-2"
}

// type = type of resources to create, name is your variable
resource "<PROVIDER>_<TYPE>" "<NAME>" {
  [CONFIG ...]
}

// use the docs, https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/instance
resource "aws_instance" "example" {
  // AMI finder https://aws.amazon.com/marketplace
  ami           = "ami-0fb653ca2d3203ac1"

  // IT https://aws.amazon.com/ec2/instance-types/
  instance_type = "t2.micro"
}
```

2. TF init
   - Scan code, download provider specific code, record download history in .lock.hcl (should be in VC)
   - `-/+` in tf plan means replace
   - You should deploy all servers in private subnet (accessible from VPC but not public internet), but we don't here

### A single server

```go
resource "aws_instance" "example" {
  ami                    = "ami-0fb653ca2d3203ac1"
  instance_type          = "t2.micro" // expressions go on right of =
  vpc_security_group_ids = [aws_security_group.instance.id]
  /*
    Resource attribute reference has the syntax
    <PROVIDER>_<TYPE>.<NAME>.<ATTRIBUTE>

    $ terraform graph
    to see the implicit dependency created
  */

  // passing a script to
  user_data = <<-EOF
              #!/bin/bash
              echo "Hello, World" > index.xhtml
              nohup busybox httpd -f -p ${var.server_port} &
              EOF // ${var.server_port} string interpolate

  // runs the ud on changes
  user_data_replace_on_change = true

  tags = {
    Name = "terraform-example"
  }
}

// As AWS by default no incoming / outgoing traffic
resource "aws_security_group" "instance" {
  name = "terraform-example-instance"

  ingress {
    from_port   = var.server_port
    to_port     = var.server_port
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    // CIDR, using to specific IP ranges
    // 0.0.0.0/0 is all ranges
  }
}

variable "server_port"{
    description = "The port the server will use for HTTP requests"
    type        = number
}

output "public_ip" {
  value       = aws_instance.example.public_ip
  description = "The public IP address of the web server"
}
// $ terraform output <OUTPUT_NAME>
```

### Output vars

```go
output "<NAME>" {
  // description =
  //sensitive
  //depends_on - rare situations, you have to give it extra hints if cannot figure out dependency graph
}
```

### Input vars

- Given `variable "server_port" {`

  - `terraform plan -var "server_port=8080"`
  - `export TF_VAR_server_port=8080`

- variable reference: use input variable from TF code, `var.<VARIABLE_NAME>`

```go
variable "number_example" {
  description = "An example of a number variable in Terraform"
  type        = number // string, number, bool, list, map, set, object, tuple, and any
  default     = 42
  //validation = custom validation rules for the input variable that go beyond basic type checks, such as enforcing minimum or maximum values on a number
  //sensitive = true, if true then doesn't log on tf plan / apply for passwords
}

// structural types
variable "object_example" {
  description = "An example of a structural type in Terraform"
  type        = object({
    name    = string
    age     = number
    tags    = list(string)
    enabled = bool
  })

  default = {
    name    = "value1"
    age     = 42
    tags    = ["a", "b", "c"]
    enabled = true
  }
}
```

### A cluster of servers

- AWS, Auto scaling group
- Below leads to a problem: launch configurations are immutable, so if you change any parameter of your launch configuration, Terraform will try to replace it. Normally, when replacing a resource, Terraform would delete the old resource first and then creates its replacement, but because your ASG now has a reference to the old resource, Terraform won’t be able to delete it.
- use a **Lifecycle setting**
- Normally, destroy then create, but with CBD, create, update references then delete

```go
resource "aws_launch_configuration" "example" {
  image_id        = "ami-0fb653ca2d3203ac1"
  instance_type   = "t2.micro"
  security_groups = [aws_security_group.instance.id]
  user_data = <<-EOF
              #!/bin/bash
              echo "Hello, World" > index.xhtml
              nohup busybox httpd -f -p ${var.server_port} &
              EOF
  // Required when using a launch configuration with an auto scaling group.
  //
  lifecycle {
    create_before_destroy = true
  }
}
resource "aws_autoscaling_group" "example" {
  launch_configuration = aws_launch_configuration.example.name
  vpc_zone_identifier  = data.aws_subnets.default.ids
  min_size = 2
  max_size = 10

  // ADDED with ALB
  target_group_arns = [aws_lb_target_group.asg.arn]
  health_check_type = "ELB" // more robust than default EC2
  // ADDED with ALB

  tag {
    key                 = "Name"
    value               = "terraform-asg-example"
    propagate_at_launch = true
  }
}
data "aws_subnets" "default" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.default.id]
  }
}

```

- **Data source**: read-only information that is fetched from the provider

```go
data "<PROVIDER>_<TYPE>" "<NAME>" {
  [CONFIG ...]
}
data "aws_vpc" "default" {
  default = true
}
// Reference, data.<PROVIDER>_<TYPE>.<NAME>.<ATTRIBUTE>
```

### Load balancer

- **Application LB**: best for http/https, level 7 of OSI
- **Network LB**: TCP, UDP, TLS, faster than ALB. OSI/level 4
- **Classic LB**: legacy

ALB

- **Listener**: what port / protocol to listen
- **Listener rule**: take requests form listener and how to match to target groups (ex. match by path )
- **Target group**: 1+ server that gets request from LB, TG performs health check on these servers

```go
resource "aws_lb" "example" {
  name               = "terraform-asg-example"
  load_balancer_type = "application"
  subnets            = [aws_security_group.alb.id]

}

resource "aws_lb_listener" "http" {
  load_balancer_arn = aws_lb.example.arn
  port              = 80
  protocol          = "HTTP"

  # By default, return a simple 404 page
  default_action {
    type = "fixed-response"

    fixed_response {
      content_type = "text/plain"
      message_body = "404: page not found"
      status_code  = 404
    }
  }
}

resource "aws_security_group" "alb" {
  name = "terraform-example-alb"

  # Allow inbound HTTP requests
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Allow all outbound requests
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_lb_target_group" "asg" {
  name     = "terraform-asg-example"
  port     = var.server_port
  protocol = "HTTP"
  vpc_id   = data.aws_vpc.default.id

  health_check {
    path                = "/"
    protocol            = "HTTP"
    matcher             = "200"
    interval            = 15
    timeout             = 3
    healthy_threshold   = 2
    unhealthy_threshold = 2
  }
}

resource "aws_lb_listener_rule" "asg" {
  listener_arn = aws_lb_listener.http.arn
  priority     = 100

  condition {
    path_pattern {
      values = ["*"]
    }
  }
  action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.asg.arn
  }
}

// update
output "alb_dns_name" {
  value       = aws_lb.example.dns_name
  description = "The domain name of the load balancer"
}

```

- https://www.airpair.com/aws/posts/building-a-scalable-web-app-on-amazon-web-services-p1

<br/>

## Terraform State

- .tfstate map resources to real world
- state file should never be edited by hand
- AWS S3 is best bet for remote backend storage, version control, encryption, durability
- **partial configuration**: omit certain parameters to resolve chicken/egg issue where TF is used to create S3 it is stored in
- Configure TF to store state in S3

```go
terraform{
 backend "s3"{
  bucket = "..."
  key = "global/s3/terraform.tfstate"
 }
}
```

### State file isolation methods

- workspaces:

  - `terraform workspace # create new`
  - `terraform workspace show`

- file layout
  - stage, prod folders
- Recommended naming
  - vpc: network
  - services: ex. each app
  - data-storage: ex. mysql, redis
  - within each component
    - variables.tf
    - outputs.tf
    - main.tf: resources and data sources
    - optionally
      - dependencies: data sources
      - providers:
      - main-xxx: if it becomes too large

### DB example

main.tf

```go
provider "aws" {
  region = "us-east-2"
}

resource "aws_db_instance" "example" {
  identifier_prefix   = "terraform-up-and-running"
  engine              = "mysql"
  allocated_storage   = 10
  instance_class      = "db.t2.micro"
  skip_final_snapshot = true
  db_name             = "example_database"

  # How should we set the username and password?
  username = var.db_username
  password = var.db_password
}

```

variables.tf

```go
variable "db_username" {
  description = "The username for the database"
  type        = string
  sensitive   = true
}

variable "db_password" {
  description = "The password for the database"
  type        = string
  sensitive   = true
}

```

outputs.tf

```go
output "address" {
  value       = aws_db_instance.example.address
  description = "Connect to the database at this endpoint"
}

output "port" {
  value       = aws_db_instance.example.port
  description = "The port the database is listening on"
}

```

- `export TF_VAR_db_username="(YOUR_DB_USERNAME)" && terraform apply`

- Reading output variables `data.terraform_remote_state.<NAME>.outputs.<ATTRIBUTE>`

```sh
user_data = <<EOF
#!/bin/bash
echo "Hello, World" >> index.xhtml
echo "${data.terraform_remote_state.db.outputs.address}" >> index.xhtml
echo "${data.terraform_remote_state.db.outputs.port}" >> index.xhtml
nohup busybox httpd -f -p ${var.server_port} &
EOF
```

- [tf built in functions](https://www.terraform.io/language/functions) `format(<FMT>, <ARGS>, ...) `

<br/>

## Reusable infra - Terraform Modules

- module = function, reusable

Folder structure

- modules/services/webserver-cluster
- stage/services/webserver-cluster
  - webserver-cluster/main.tf
- `terraform init`

```go
provider "aws" {
  region = "us-east-2"
}

module "webserver_cluster" {
  source = "../../../modules/services/webserver-cluster"
  cluser_name = "webservers-stage" // pass args to module
}
```

```go
locals {
  http_port    = 80
  any_port     = 0
  any_protocol = "-1"
  tcp_protocol = "tcp"
  all_ips      = ["0.0.0.0/0"]
}
local.<NAME> // access
```

- `module.<MODULE_NAME>.<OUTPUT_NAME>`

  - accessing module output vars

- Versioned modules via referencing module code on git
  - [TF docs on source](https://www.terraform.io/language/modules/sources)

```go
module "webserver_cluster" {
  source = "github.com/foo/modules//services/webserver-cluster?ref=v0.0.1"

  cluster_name           = "webservers-stage"
  db_remote_state_bucket = "(YOUR_BUCKET_NAME)"
  db_remote_state_key    = "stage/data-stores/mysql/terraform.tfstate"

  instance_type = "t2.micro"
  min_size      = 2
  max_size      = 2
}
```

<br/>

## TF loops, if-state, deployments

```go
variable "user_names" {
  description = "Create IAM users with these names"
  type        = list(string)
  default     = ["neo", "trinity", "morpheus"]
}

resource "aws_iam_user" "example" {
  count = length(var.user_names)
  name  = var.user_names[count.index]
}

output "user_arns" {
  value       = module.users[*].user_arn
  description = "The ARNs of the created IAM users"
}
```

- use create_before_destroy for 0 downtime deployments
- TF plan only looks at resources in tf state plan, doesn't consider AWS created else where
- Once you start using TF, only use TF. Use import command for existing
  - `terraform import aws_iam_user.existing_user yevgeniy.brikman`

<br/>

## Secret management

<br/>

## Working with multiple providers

- multiple AWS regions

### Docker crash course

- `docker run <IMAGE> [COMMAND]`
- `docker run -it ubuntu:20.04 bash`
- `docker ps -a`
- `docker start -ia <CONTAINER_ID>`
- `docker run -p 5000:5000 training/webapp`
  - Simple port 5000 hello world
- `docker rm <CONTAINER_ID>`
  - Or with `--rm` tag

### K8 crash course

- K8 = control plane + work nodes
- Download docker desktop and enable k8
- Install `kubectl`
- `$HOME/.kube/config` tells what cluster kubectl connects to
- `kubectl config use-context docker-desktop`
- `kubectl get nodes`
  - local computer is only node
- To deploy in k8, you create k8 objects: persistent entities which allow you to write to the k8 cluster that record your intent
- reconcilation loop: continuously checks objects stored to make state of cluster match your intent
- k8 deployment object: you tell it how many replicas and settings for those images
- k8 service: way to expose web app running k8 as a networked service
  - Ex. use k8 service to configure load balancer that exposes public endpoint and distributes traffic across replicas in k8 deployment
- To interact with k8, create YAML files describing what you want then `kubectl apply`
- Other way, use helm / TF module, ex. ` k8s-app`
- k8, pods are deployed, groups of containers meant to be deployed together
- `kubectl get deployments`
- `kubectl get pods`
- `kubectl get services`

### EKS AWS deploy example

- using TF

## PROD grade TF code - modules
