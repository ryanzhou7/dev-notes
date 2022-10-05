## Tutorials

[Tutorial: Create a web server and an Amazon RDS DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/TUT_WebAppWithRDS.html)

- [Launch an EC2 instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.LaunchEC2.html)
  - Choose amazon linux, allow ssh, http, https
- [Create a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.CreateDBInstance.html)
  - compute resource, (connect to ec2)
- [Install a web server on your EC2 instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.CreateWebServer.html)

  - Apache PHP

- [Terraform](https://registry.terraform.io/modules/terraform-aws-modules/rds/aws/latest/examples/complete-postgres)

```
module "rds" {
  source  = "terraform-aws-modules/rds/aws"
  version = "5.1.0"
  # insert the 1 required variable here
}
```
