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
