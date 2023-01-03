terraform {
  cloud {
    organization = "platinumVinyls"

    workspaces {
      name = "platinum"
    }
  }
}

variable "GOOGLE_APPLICATION_CREDENTIALS" {
  type = string
  sensitive = false
  description = "Google Cloud service account credentials"
}

provider "google" {
    project = "ceri-m1-ecommerce-2022"
    region = "europe-west1"
    credentials = var.GOOGLE_APPLICATION_CREDENTIALS 
}

data "google_secret_manager_secret" "address" {
  secret_id = "mysql-address"
}

data "google_secret_manager_secret" "database" {
  secret_id = "mysql-database-orangedog"
}

data "google_secret_manager_secret" "password" {
  secret_id = "mysql-password-orangedog"
}



resource "google_cloud_run_service" "backend" {

  name     = "orangedog-backend"
  location = "europe-west1"

  template {
    spec {
      service_account_name = "terraform-orangedog@ceri-m1-ecommerce-2022.iam.gserviceaccount.com"
      containers {
        image = "europe-west1-docker.pkg.dev/ceri-m1-ecommerce-2022/orangedog/back-end"
        env {
          name = "DATABASE_ADDRESS"
          value_from {
            secret_key_ref {
              name = data.google_secret_manager_secret.address.secret_id
              key = "latest"
            }
          }
        }
        env {
          name = "DATABASE_NAME"
          value_from {
            secret_key_ref {
              name = data.google_secret_manager_secret.database.secret_id
              key = "latest"
            }
          }
        }
        env {
          name = "PASSWORD"
          value_from {
            secret_key_ref {
              name = data.google_secret_manager_secret.password.secret_id
              key = "latest"
            }
          }
        }
        env {
          name = "DATABASE_USER"
          value = "orangedog"
        }
        ports {
          container_port = 5000
        }
      }
    }

    metadata {
      annotations = {
        "autoscaling.knative.dev/maxScale" = "1"
      }
    }
  }

  traffic {
    percent = 100
    latest_revision = true
  }
}

output "url" {
  value       = google_cloud_run_service.backend.status[0].url
  sensitive   = false
  description = "description"
  depends_on  = []
}

resource "google_cloud_run_service" "frontend" {

  name     = "orangedog-frontend"
  location = "europe-west1"

  template {
    spec {
      service_account_name = "terraform-orangedog@ceri-m1-ecommerce-2022.iam.gserviceaccount.com"
      containers {
        image = "europe-west1-docker.pkg.dev/ceri-m1-ecommerce-2022/orangedog/front-end"
        env {
          name = "BACKEND_URL"
          value = google_cloud_run_service.backend.status[0].url
        }
        ports {
          container_port = 80
        }
      }
    }

    metadata {
      annotations = {
        "autoscaling.knative.dev/maxScale" = "1"
      }
    }
  }

  traffic {
    percent = 100
    latest_revision = true
  }
}

output "url" {
  value       = google_cloud_run_service.frontend.status[0].url
  sensitive   = false
  description = "description"
  depends_on  = []
}

resource "google_cloud_run_service_iam_member" "invokers" {
  location = google_cloud_run_service.backend.location
  service = google_cloud_run_service.backend.name
  role    = "roles/run.invoker"
  member  = "allUsers"
}
