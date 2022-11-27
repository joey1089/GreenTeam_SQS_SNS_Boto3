#Here we use Boto3's module method create_queue to create sqs messages
import boto3


sqs = boto3.resource('sqs') # create service request objects
queue = sqs.create_queue(QueueName='Project-Week-15-TestQueue') # Create the SQS queue
print('Queue URL',queue.url) # url for cloudwatch logs
