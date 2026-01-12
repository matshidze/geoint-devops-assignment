output "network_name" {
  description = "Created Docker network name"
  value       = docker_network.geoint_net.name
}

output "network_id" {
  description = "Created Docker network ID"
  value       = docker_network.geoint_net.id
}

output "pg_volume_name" {
  description = "Created Docker volume name"
  value       = docker_volume.geoint_pgdata.name
}

output "pg_volume_id" {
  description = "Created Docker volume ID"
  value       = docker_volume.geoint_pgdata.id
}
