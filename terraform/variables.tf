variable "network_name" {
  type        = string
  description = "Docker network name used for the GeoInt stack"
  default     = "geoint-assignment-net"
}

variable "pg_volume_name" {
  type        = string
  description = "Docker volume name for Postgres persistent data"
  default     = "geoint_pgdata"
}
