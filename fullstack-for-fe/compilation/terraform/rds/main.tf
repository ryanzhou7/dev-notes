resource "aws_db_instance" "default" {
  # The amount of storage in gibibytes (GiB) to allocate for the DB instance.
  # pg min = 20
  allocated_storage    = 20 
  identifier            = "myrds1" 
  db_name              = "mydb1"
  engine               = "postgres"
  engine_version       = "14.4"

  # The compute and memory capacity of the DB instance (ec2)
  instance_class       = "db.t3.micro"
  username             = "db_username"
  password             = "db_password89898918989"

  vpc_security_group_ids = ["sg-0133e65ba6440731f"]
  auto_minor_version_upgrade = false
  publicly_accessible    = true
  skip_final_snapshot  = true
}