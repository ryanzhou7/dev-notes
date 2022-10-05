# Terraform getting started

## Intro

- IaC: manage infrastructure with config files rather than GUI
  - safe, consistent, repeatable
- Terraform plugins aka [Providers](https://registry.terraform.io/browse/providers): allow terraform to interact with cloud platforms
- Provider define individual units of infra as resources, resources are composed into reusable terraform configurations called **modules**
- Terraform config language is declarative: it describes the end-state for your infra (as opposed to step by step). Dependencies are auto created / destroyed in the correct order
- To deploy infra with terraform

  - Scope - Identify the infrastructure for your project.
  - Author - Write the configuration for your infrastructure.
  - Initialize - Install the plugins Terraform needs to manage the infrastructure.
  - Plan - Preview the changes Terraform will make to match your configuration.
  - Apply - Make the planned changes.

## Install

- `brew tap hashicorp/tap`
- `brew install hashicorp/tap/terraform`
- `terraform -help` then `terraform -help plan`

## Local

- `open -a Docker`
- `mkdir learn-terraform-docker-container && cd learn-terraform-docker-container`
- `terraform init`: downloads plugin that allows terraform to interact with docker
- `terraform apply`: to provision nginx container, will show you provision
- `docker ps`: to see the resource
- `terraform destroy`: to destroy
