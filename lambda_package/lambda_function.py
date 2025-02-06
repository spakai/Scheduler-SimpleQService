import json
import boto3
import os
from datetime import datetime, timezone

sqs = boto3.client('sqs')
queue_url = os.environ['QUEUE_URL']

def lambda_handler(event, _):
    for record in event['Records']:
        message = json.loads(record['body'])
        task_id = message['task_id']
        scheduled_time = message['scheduled_time']  # Assume this is a timestamp

        current_time = datetime.now(timezone.utc)
        scheduled_time_dt = datetime.strptime(scheduled_time, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)

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
            # Ensure delay_seconds is within the valid range
            delay_seconds = max(0, min(delay_seconds, 43199))
            print(f"Rescheduling task {task_id} to run in {delay_seconds} seconds")
            sqs.change_message_visibility(
                QueueUrl=queue_url,
                ReceiptHandle=record['receiptHandle'],
                VisibilityTimeout=delay_seconds
            )

    return {
        'statusCode': 200,
        'body': json.dumps('Successfully processed messages')
    }
