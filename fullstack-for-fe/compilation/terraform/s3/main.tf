# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket#example-usage
# https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket_website_configuration
resource "aws_s3_bucket" "example" {
  bucket = "b3ucket"
  acl    = "public-read"
  policy = file("policy.json")
  website {
    index_document = "index.html"
  }
}