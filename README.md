# GeoInt DevOps Assignment

This project demonstrates the design and implementation of a complete DevOps pipeline for a containerized Flask application. It includes containerization, monitoring, infrastructure as code, CI/CD automation, and Kubernetes-based deployment to illustrate production-ready DevOps practices.

---

## Architecture Overview

Components:
- Flask web application
- PostgreSQL database
- Docker & Docker Compose for local development
- Prometheus for monitoring
- Terraform for infrastructure as code (IaC)
- GitHub Actions for CI/CD
- Kubernetes for scalable deployment

Flow:
Developer | GitHub | CI Pipeline | Docker Build | Kubernetes Deployment | Monitoring

---

## Features

- Containerized Flask application with PostgreSQL backend
- Prometheus metrics exposed at '/metrics'
- Terraform modules for infrastructure provisioning
- GitHub Actions pipeline for automated validation
- Kubernetes manifests with:
  - Deployments
  - StatefulSets
  - Services
  - Ingress
  - Horizontal Pod Autoscaler (HPA)
  - ConfigMaps and Secrets

---

## Tech Stack

- Python (Flask)
- PostgreSQL
- Docker, Docker Compose
- Prometheus
- Terraform
- GitHub Actions
- Kubernetes (Minikube / Docker Desktop)

---

## Running Locally (Docker Compose)

docker compose up --build
