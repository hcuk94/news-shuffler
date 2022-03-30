// Local Vars
locals {
  function_name = "themorningreport-${var.environment_name}"
}

// S3 bucket for app files
resource "aws_s3_bucket" "themorningreport_bucket" {
  bucket = "themorningreport-bucket-${var.environment_name}"
}

// Move the application files into the S3 bucket
resource "aws_s3_bucket_object" "themorningreport_bucket_object" {
  bucket = aws_s3_bucket.themorningreport_bucket.bucket
  key = "themorningreport_lambda.zip"
  source = var.application_file
  etag = filemd5(var.application_file)
}

// Set up IAM role
resource "aws_iam_role" "themorningreport_lambda_role" {
  name = "lambda_execution_role-themorningreport-${var.environment_name}"
  assume_role_policy = data.aws_iam_policy_document.lambda_assume_role.json
}

// Assign policy to IAM role
resource  "aws_iam_role_policy_attachment" "lambda_role_policy" {
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
  role = aws_iam_role.themorningreport_lambda_role.name
}

// Assign policy to IAM role
resource  "aws_iam_role_policy_attachment" "s3_role_policy" {
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
  role = aws_iam_role.themorningreport_lambda_role.name
}

// Allow lambda service to assume role
data "aws_iam_policy_document" "lambda_assume_role" {
  statement {
    effect = "Allow"
    principals {
      type = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
    actions = ["sts:AssumeRole"]
  }
}

// Create a log group and set retention
resource "aws_cloudwatch_log_group" "log_group" {
  name              = "/aws/lambda/${local.function_name}"
  retention_in_days = 14
}

resource "aws_lambda_function" "themorningreport_function" {
  function_name = local.function_name
  handler = "handler.lambda_handler"
  role = aws_iam_role.themorningreport_lambda_role.arn
  runtime = "python3.10"
  publish = true
  memory_size = 2048
  s3_bucket = aws_s3_bucket.themorningreport_bucket.bucket
  s3_key = aws_s3_bucket_object.themorningreport_bucket_object.key
  s3_object_version = aws_s3_bucket_object.themorningreport_bucket_object.version_id
}

resource "aws_lambda_permission" "apigw_lambda_permission" {
  action = "lambda:InvokeFunction"
  function_name = aws_lambda_function.themorningreport_function.function_name
  principal = "apigateway.amazonaws.com"
}