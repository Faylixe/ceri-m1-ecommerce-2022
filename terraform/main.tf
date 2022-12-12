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
  secret_id = "mysql.address"
}

resource "google_cloud_run_service" "backend" {

  name     = "backend"
  location = "europe-west1"

  template {
    spec {
      service_account_name = "terraform-orangedog@ceri-m1-ecommerce-2022.iam.gserviceaccount.com"
      container {
        env {
          name = "DATABASE_ADDRESS"
          value_from {
            secret_key_ref {
              name = "data_google_secret_manager_secret address secret_id"
            }
          }
        }
      }
    }
  }
}
