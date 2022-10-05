resource "aws_security_group" "allow_tls" {
  name        = "Allow all traffice from anywhere - tf"
  description = "Allow all traffice from anywhere"

  ingress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }
  
  # allow all 
  # By default, AWS creates an ALLOW ALL egress rule when creating a new Security Group inside of a VPC. When creating a new Security Group inside a VPC, Terraform will remove this default rule, and require you specifically re-create it if you desire that rule. We feel this leads to fewer surprises in terms of controlling your egress rules. If you desire this rule to be in place, you can use this egress block:
  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }
}