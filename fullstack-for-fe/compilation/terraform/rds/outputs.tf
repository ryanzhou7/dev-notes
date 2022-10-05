output "rds_endpoint" {
  description = "Endpoint to connect"
  value       = aws_db_instance.default.endpoint
}