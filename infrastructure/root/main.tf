module "lambda" {
  source = "./lambda"
  application_file = var.application_file
  environment_name = var.environment_name
}