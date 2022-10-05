terraform {
  required_providers { # to provision infra
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}
# specific config for aws
provider "aws" {
  region = "us-west-2"
}
# amis are region specific 

# resources always follows by 2 strings, "resource type" and "resource name"
# provider "aws" prefixes res type
# RT + RN = unique ID
# See arguments for res blocks for this provider https://registry.terraform.io/providers/hashicorp/aws/latest/docs
# EC2 https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/instance
# https://cloud-images.ubuntu.com/locator/ec2/
resource "aws_instance" "app_server" {
  # these then configure the resource
   # 830c94e3 -> 08d70e59c07c61a3a
  ami           = "ami-08d70e59c07c61a3a"
  instance_type = "t2.micro"
  tags = {
    Name = "ExampleAppServerInstance1"
  }
}
