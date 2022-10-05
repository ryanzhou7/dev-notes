provider "aws" {
  region = "us-west-1"
}
module "server_1" {
  source = "../server"
  name = "server-1" # passing this to vars to server
}
module "server_2" {
  source = "../server"
  name = "server-2"
}