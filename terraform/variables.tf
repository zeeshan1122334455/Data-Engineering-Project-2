variable "ACCESS_KEY" {
  type        = string
  description = "access key of aws account"
}
variable "SECRET_KEY" {
  type        = string
  description = "secret key of aws account"
}

variable "REDSHIFT_ARN" {
  type = string
  description = "arn role for redshift cluster"
}