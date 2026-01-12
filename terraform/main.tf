terraform {
  required_version = ">= 1.5.0"

  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

# Demonstration resources: a network and a volume
resource "docker_network" "geoint_net" {
  name = var.network_name
}

resource "docker_volume" "geoint_pgdata" {
  name = var.pg_volume_name
}
