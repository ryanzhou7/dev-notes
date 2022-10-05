provider "aws" {
  region = "us-east-2"
}
module "eks_cluster" {
  source = "github.com/brikis98/terraform-up-and-running-code//code/terraform/07-working-with-multiple-providers/modules/services/eks-cluster?ref=v0.3.0"
}