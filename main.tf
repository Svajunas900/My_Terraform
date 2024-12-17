variable "function_name" {
  type = string
}

data "aws_lambda_function" "existing" {
  function_name = var.function_name
}