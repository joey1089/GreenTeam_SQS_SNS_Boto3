#Here we use Boto3 to send sqs messages
import boto3


sqs = boto3.resource('sqs') # create service request objects
queue = sqs.create_queue(QueueName='Project-Week-15-TestQueue') # Create the SQS queue
print(queue.url) # url for msg
