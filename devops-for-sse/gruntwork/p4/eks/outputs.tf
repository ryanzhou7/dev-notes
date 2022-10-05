output "cluster_arn" {
  value       = module.eks_cluster.cluster_arn
  description = "ARN of the EKS cluster"
}
output "cluster_endpoint" {
  value       = module.eks_cluster.cluster_endpoint
  description = "Endpoint of the EKS cluster"
}