[AWS](https://learn.hashicorp.com/tutorials/terraform/aws-build?in=terraform/aws-get-started)

## Install terraform

- [Vscode extension](https://marketplace.visualstudio.com/items?itemName=HashiCorp.terraform)
- `export AWS_ACCESS_KEY_ID=`
- `export AWS_SECRET_ACCESS_KEY=`
- `terraform init`
  - DLs the aws provider and installs in .terraform sub directory, produces .terraform.lock.hcl
  - https://github.com/github/gitignore/blob/main/Terraform.gitignore
- `terraform fmt`
  - update formats curr dir, returns formatted files
- `terraform validate`
  - syntax check

## Build infrastructure - see main.tf

- `terraform apply`
  - - means tf will create this resource, in the indent it shows the attributes that will be set
- terraform.tfstate produced, stores IDs and props of the resources so it can update it. sensitive info
- `terraform show`

## Change infrastructure

- `ami = "ami-08d70e59c07c61a3a"` change
- "Plan: 1 to add, 0 to change, 1 to destroy." since with ami cannot change without recreation

## Destroy infrastructure

- `terraform destroy`
