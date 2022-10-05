# Removed 
# provider "aws" {
#   region = "us-west-1"
# }

resource "aws_instance" "example" {
  ami           = var.ami
  instance_type = var.instance_type
  key_name      = var.key_name
  
  vpc_security_group_ids = [aws_security_group.instance.id]
  tags = {
    Name = var.name
  }
}

resource "aws_security_group" "instance" {
  name = var.name
  ingress {
    from_port   = var.ssh_port
    to_port     = var.ssh_port
    protocol    = "tcp"
    cidr_blocks = var.allow_ssh_from_cidrs
  }
}