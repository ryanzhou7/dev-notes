provider "kubernetes" {
  config_path = "~/.kube/config"
}
module "simple_webapp" {
  source = "github.com/brikis98/terraform-up-and-running-code//code/terraform/07-working-with-multiple-providers/modules/services/k8s-app?ref=v0.3.0"
  name           = "simple-webapp"
  image          = "training/webapp"
  replicas       = 2
  container_port = 5000
}