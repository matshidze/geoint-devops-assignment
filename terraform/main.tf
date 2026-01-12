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

# Example: demonstrate provisioning concept via Docker provider
resource "docker_network" "app_net" {
  name = var.network_name
}
