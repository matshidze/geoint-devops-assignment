output "network_id" {
  value       = docker_network.app_net.id
  description = "Created Docker network ID"
}

output "network_name" {
  value       = docker_network.app_net.name
  description = "Created Docker network name"
}
