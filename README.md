# SQS and Lambda Project

This project sets up an AWS infrastructure using Terraform that includes an SQS queue and a Lambda function. The Lambda function processes messages from the SQS queue with specific handling for message visibility and delay.

## Project Structure

- `main.tf`: Contains the main Terraform configuration, defining the SQS queue, Lambda function, and IAM roles.
- `variables.tf`: Defines input variables for the configuration, such as queue name, delay seconds, and visibility timeout.
- `outputs.tf`: Specifies the outputs of the configuration, including the SQS queue URL and Lambda function ARN.
- `provider.tf`: Configures the AWS provider and specifies the region for resource creation.
- `README.md`: Documentation for the project.

## Setup Instructions

1. **Install Terraform**: Ensure you have Terraform installed on your machine. You can download it from the [Terraform website](https://www.terraform.io/downloads.html).

2. **Configure AWS Credentials**: Make sure your AWS credentials are configured. You can set them up using the AWS CLI or by creating a `~/.aws/credentials` file.

3. **Clone the Repository**: Clone this repository to your local machine.

4. **Navigate to the Project Directory**: Change into the project directory:
   ```
   cd sqs_lambda_project
   ```

5. **Initialize Terraform**: Run the following command to initialize the Terraform configuration:
   ```
   terraform init
   ```

6. **Plan the Deployment**: Generate an execution plan with:
   ```
   terraform plan
   ```

7. **Apply the Configuration**: Deploy the resources by running:
   ```
   terraform apply
   ```

8. **Usage**: Once deployed, you can send messages to the SQS queue. The Lambda function will process these messages based on the specified delay and visibility settings.

## Additional Information

- Ensure that the Lambda function has the necessary permissions to access the SQS queue.
- Modify the `variables.tf` file to customize the queue name, delay seconds, and visibility timeout as needed.
- Monitor the Lambda function and SQS queue in the AWS Management Console for logs and metrics.