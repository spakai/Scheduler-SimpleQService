# SQS and Lambda Project

This project sets up an AWS infrastructure using Terraform that includes an SQS queue and a Lambda function. The Lambda function processes messages from the SQS queue with specific handling for message visibility and delay.



![Architecture](SQSLambda.png)


## Project Structure

- `main.tf`: Contains the main configuration for the Terraform infrastructure, defining the AWS EventBridge rule and the Lambda function.
- `variables.tf`: Defines input variables for the Terraform configuration, specifying types and default values.
- `outputs.tf`: Specifies output values that Terraform will display after applying the configuration, including resource ARNs.
- `provider.tf`: Configures the Terraform provider, typically the AWS provider with necessary authentication details.

## Getting Started

### Prerequisites

- Terraform installed on your machine.
- AWS account with appropriate permissions to create resources.
- AWS CLI configured with your credentials.


### Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd Scheduler-SimpleQService
   ```

1.1 Prepare lambda package:
   ```
   cd lambda_package
   pip install --target ./package boto3
   zip -r ../lambda.zip .
   cd ..
   ```

2. Initialize Terraform:
   ```
   terraform init
   ```

3. Review and modify the `variables.tf` file as needed to set your desired configurations.

4. Plan the deployment:
   ```
   terraform plan
   ```

5. Apply the configuration:
   ```
   terraform apply
   ```



6. Add items to SQS. one that has expired and one that would expire in the future:
```
aws sqs send-message-batch  --queue-url $sqs_queue_url --entries '[
        {
            "Id": "msg1",
            "MessageBody": "{\"task_id\": \"19780512\", \"scheduled_time\": \"2025-02-04T12:00:00Z\"}"
        },
        {
            "Id": "msg2",
            "MessageBody": "{\"task_id\": \"1980917\", \"scheduled_time\": \"2025-02-07T00:00:00Z\"}"
        }
    ]'     --region us-east-1
    
```

7. after a minute or so , check logs
```
#First task
2025-02-06T23:16:53.095+08:00
Running task 19780512

Running task 19780512

#Second task
2025-02-06T23:16:53.103+08:00
Rescheduling task 1980917 to run in 31386 seconds

```


### Outputs

After applying the configuration, Terraform will display the output values defined in `outputs.tf`, including the ARN of the created resources.   

### Cleanup

To remove the resources created by this project, run:
```
terraform destroy
``` 

## License

This project is licensed under the MIT License.
