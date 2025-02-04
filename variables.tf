variable "queue_name" {
  description = "The name of the SQS queue"
  type        = string
  default     = "my_queue"
}

variable "delay_seconds" {
  description = "The delay in seconds for messages in the SQS queue"
  type        = number
  default     = 15
}

variable "visibility_timeout" {
  description = "The visibility timeout for the SQS messages"
  type        = number
  default     = 43200  # 12 hours in seconds
}
