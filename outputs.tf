output "sqs_queue_url" {
  value = aws_sqs_queue.my_queue.id
}

output "lambda_function_arn" {
  value = aws_lambda_function.my_lambda.arn
}