terraform {
  cloud {
    organization = "platinumVinyls"

    workspaces {
      name = "platinum"
    }
  }
}

provider "google" {
    project = "ceri-m1-ecommerce-2022"
    region = "europe-west1"
}

data "google_secret_manager_secret" "address" {
  secret_id = "mysql-address"
}

data "google_secret_manager_secret" "database" {
  secret_id = "mysql-database-orangedog"
}

data "google_secret_manager_secret" "user" {
  secret_id = "mysql-user-orangedog"
}

data "google_secret_manager_secret" "password" {
  secret_id = "mysql-password-orangedog"
}

resource "google_cloud_run_service" "backend" {

  name     = "backend"
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
      }
    }
  }
}
