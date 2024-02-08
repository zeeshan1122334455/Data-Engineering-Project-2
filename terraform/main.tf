terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.35.0"
    }
  }
}

provider "aws" {
  region     = "ap-south-1"
  access_key = var.ACCESS_KEY
  secret_key = var.SECRET_KEY
}
resource "aws_s3_bucket" "example" {
  bucket        = "farans-bucket"
  force_destroy = true
}