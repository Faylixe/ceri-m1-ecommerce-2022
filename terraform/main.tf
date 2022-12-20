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

data "google_secret_manager_secret" "address" {
    secret_id="mysql-address"
}

resource "google_cloud_run_service" "backend" {
    name     = "whitehorse"
    location = "europe-west1"

    template{
        spec{
            service_account_name = "terraform-whitehorse@ceri-m1-ecommerce-2022.iam.gserviceaccount.com"
            containers{
                env{
                    name="varPourConnexionBDDGCPDeLea"
                    value_from{
                        secret_key_ref{
                            name=data_google.secret_manager_secret.address.secret.secret_id
                            key="latest"
                        }
                    }
                }
            }
        }
    }
}
