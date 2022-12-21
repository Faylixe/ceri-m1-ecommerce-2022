terraform{
    cloud{
        organization = "Ceri"
        workspaces{
            name="MasterCodeuses"
        }
    }
}

provider "google"{
    project="ceri-m1-ecommerce-2022"
    region="europe-west1"
}

data "google_secret_manager_secret" "username" {
    secret_id="mysql-user-whitehorse"
}

data "google_secret_manager_secret" "password" {
    secret_id="mysql-password-whitehorse"
}

data "google_secret_manager_secret" "database" {
    secret_id="mysql-database-whitehorse"
}

data "google_secret_manager_secret" "host" {
    secret_id="mysql-address"
}

resource "google_cloud_run_service" "backend" {
    location = google_cloud_run_service.backend.location
    service = google_cloud_run_service.backend.name
    role    = "roles/run.invoker"
    member  = "allUsers"

    template{
        spec{
            service_account_name = "terraform-whitehorse@ceri-m1-ecommerce-2022.iam.gserviceaccount.com"
            containers{
                image = "europe-west1-docker.pkg.dev/ceri-m1-ecommerce-2022/whitehorse/backend:0.0.1"
                env{
                    name="USERNAME"
                    value_from{
                        secret_key_ref{
                            name=data_google.secret_manager_secret.username.secret.secret_id
                            key="latest"
                        }
                    }
                }
                env{
                    name="PASSWORD"
                    value_from{
                        secret_key_ref{
                            name=data_google.secret_manager_secret.password.secret.secret_id
                            key="latest"
                        }
                    }
                }
                env{
                    name="HOST"
                    value_from{
                        secret_key_ref{
                            name=data_google.secret_manager_secret.host.secret.secret_id
                            key="latest"
                        }
                    }
                }
                env{
                    name = "PORT"
                    value = 3306
                }
                env{
                    name="DATABASE"
                    value_from{
                        secret_key_ref{
                            name=data_google.secret_manager_secret.database.secret.secret_id
                            key="latest"
                        }
                    }
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
resource "google_cloud_run_service" "frontend" {
  name     = "frontend"
  location = "europe-west1"

  template {
    spec {
      service_account_name = "terraform-whitehorse@ceri-m1-ecommerce-2022.iam.gserviceaccount.com"
      containers {
        image = "europe-west1-docker.pkg.dev/ceri-m1-ecommerce-2022/whitehorse/frontend:0.0.1"
        env {
          name = "BACKEND_URL"
          value = resource.google_cloud_run_service.backend.url
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
