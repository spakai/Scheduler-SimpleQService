import json
import boto3
import os
import time
from datetime import datetime
\

sqs = boto3.client('sqs')
queue_url = os.environ['QUEUE_URL']

def lambda_handler(event, context):
    for record in event['Records']:
        message = json.loads(record['body'])
        task_id = message['task_id']
        scheduled_time = message['scheduled_time']  # Assume this is a timestamp

        current_time = datetime.utcnow()
        scheduled_time_dt = datetime.strptime(scheduled_time, '%Y-%m-%dT%H:%M:%SZ')

        if current_time >= scheduled_time_dt:
            # Time to run the task
            print(f"Running task {task_id}")
            # Add your task processing logic here

            # Delete the message from the queue
            sqs.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=record['receiptHandle']
            )
        else:
            # Not yet time to run the task, change message visibility
            delay_seconds = int((scheduled_time_dt - current_time).total_seconds())
            delay_seconds = min(delay_seconds, 12 * 60 * 60)  # Max 12 hours

            sqs.change_message_visibility(
                QueueUrl=queue_url,
                ReceiptHandle=record['receiptHandle'],
                VisibilityTimeout=delay_seconds
            )

    return {
        'statusCode': 200,
        'body': json.dumps('Successfully processed messages')
    }