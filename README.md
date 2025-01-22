# Python Flask Api
Python flask Api deployed on Google Cloud Run (Containerized Function)

## Prerequisite

Following are the list of libraries required for this API.

- Docker
- Google Cloud Console
- Python 3.13
- Flask 3.1.x


## How to Run
Perform the below command from prompt.
- pip install Flask - To install the flask.
- python app.py - To run the API

## Terraform

Below the sample terraform module for Cloud Run functions

```
resource "google_cloud_run_v2_service" "default" {
  name     = "cloud-run-flask-api"
  location = "europe-west2"
  deletion_protection = false
  ingress = "INGRESS_TRAFFIC_ALL"

  template {
    containers {
      image = "us-docker.pkg.dev/cloudrun/container/hello"
      resources {
        limits = {
          cpu    = "2"
          memory = "1024Mi"
        }
      }
    }
  }
}

```

## About

Containerized Python Flast Api (with UI to add and list items), just to demostrate how to get and post the data on Flask Api via Python.

## Additional 
- [Install Python](https://www.python.org/doc/versions/)
- [Flask](https://flask.palletsprojects.com/en/stable/)
- [Google github actions](https://github.com/google-github-actions/auth)
- [Terrafom Google Cloud Run](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service)