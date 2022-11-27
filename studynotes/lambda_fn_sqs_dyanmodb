import boto3
import json
import datetime

sqs = boto3.resource('sqs')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
	# Receive messages from sqs queue
	queue = sqs.get_queue_by_name(QueueName=QUEUE_NAME)

    print("ApproximateNumberOfMessages :",queue.attributes.get('ApproximateNumberOfMessages'))
    
    for message in queue.receive_messages(
        MaxNumberOfMessages = int(MAX_QUEUE_MESSAGES)):
        print(message)

        # Write message to Dynamodb
        table = dynamodb.Table(DYNAMODB_TABLE)

        response = table.put_item(
            Item={
                'MessageId':message.message_id,
                'Body':message.body,
                'Timestamp': datetime.now().isoformat()
            }
        )
        print("Wrote message to DynamoDB : ", json.dumps(response))

        # Delete SQS message
        message.delete()
        print("Deleted message :", message.message_id)


# From hands on lab session on ACG 
# https://learn.acloud.guru/handson/c11ca4ba-f942-4a5b-9c75-ad3ff8134a97/course/d15d3060-fa99-4dbd-90c1-c1b9abb70f53
#https://raw.githubusercontent.com/ACloudGuru-Resources/SQSLambdaTriggers/master/lambda_function.py
#  
#
from datetime import datetime
import json
import os
import boto3

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    # Count items in the Lambda event 
    no_messages = str(len(event['Records']))
    print("Found " +no_messages +" messages to process.")

    for message in event['Records']:

        print(message)

        # Write message to DynamoDB
        table = dynamodb.Table('Message')

        response = table.put_item(
            Item={
                'MessageId': message['messageId'],
                'Body': message['body'],
                'Timestamp': datetime.now().isoformat()
            }
        )
        print("Wrote message to DynamoDB:", json.dumps(response))

#
#
#
[cloud_user@ip-10-1-10-88 ~]$ cat send_message.py 
#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
import argparse
import logging
import sys
from time import sleep
import boto3
from faker import Faker


parser = argparse.ArgumentParser()
parser.add_argument("--queue-name", "-q", required=True,
                    help="SQS queue name")
parser.add_argument("--interval", "-i", required=True,
                    help="timer interval", type=float)
parser.add_argument("--message", "-m", help="message to send")
parser.add_argument("--log", "-l", default="INFO",
                    help="logging level")
args = parser.parse_args()

if args.log:
    logging.basicConfig(
        format='[%(levelname)s] %(message)s', level=args.log)

else:
    parser.print_help(sys.stderr)

sqs = boto3.client('sqs')

response = sqs.get_queue_url(QueueName=args.queue_name)

queue_url = response['QueueUrl']

logging.info(queue_url)

while True:
    message = args.message
    if not args.message:
        fake = Faker()
        message = fake.text()

    logging.info('Sending message: ' + message)

    response = sqs.send_message(
        QueueUrl=queue_url, MessageBody=message)

    logging.info('MessageId: ' + response['MessageId'])
    sleep(args.interval)

#
#
#
# Triggering AWS Lambda from Amazon SQS
# Introduction
# In this hands-on AWS lab, you will learn how to trigger a Lambda function using SQS. 
# This Lambda function will process messages from the SQS queue and insert the message data as 
# records into a DynamoDB table.

# Solution
# Log in to the AWS Management Console using the credentials provided on the lab instructions page. 
# Make sure you're using the us-east-1 (N. Virginia) region.

# Create the Lambda Function
# In the search bar on top, enter "lambda".
# From the search results, select Lambda.
# Click the Create function button.
# On the Create function page, select Author from scratch.
# Under Basic Information, set the following parameters for each field:
# Function name: Enter "SQSDynamoDB".
# Runtime: Select Python 3.9 from the dropdown menu.
# Execution role: Select Use an existing role.
# Existing role: Select lambda-execution-role from the dropdown menu,
# Click the Create function button.
# Create the SQS Trigger
# Click the + Add trigger button.
# Under Trigger configuration, enter "sqs" in the search bar.
# From the search results, select Simple Queue Service.
# Under SQS queue, click the search bar and select Messages.
# Click Add.
# Copy the Source Code into the Lambda Function
# Under the + Add trigger button, click the Code tab.
# On the left side, double-click on lambda_function.py.
# Delete the contents of the function.
# Navigate to the link below to the source code for lambda_function.py
# https://raw.githubusercontent.com/ACloudGuru-Resources/SQSLambdaTriggers/master/lambda_function.py. 
# 6. Copy the code. 7. Return to the AWS console and paste the code into the lambda_function.py code box. 
# 8. Click the Deploy button.

# Log In to the EC2 Instance and Test the Script
# In the search bar on top of the console, enter "sqs".

# From the search results, select Simple Queue Service.

# Click Messages.

# Click the Monitoring tab to monitor our SQS messages.

# In the search bar on top, enter "ec2".

# From the search results, select EC2 and open it in a new browser tab or window.

# Under Resources, click Instances (running).

# In the existing instance available, click the checkbox next to its name.

# Click the Connect button at the top.

# Click Connect at the bottom to open a shell and access the command line.

# In the shell, become the cloud_user role:

# su - cloud_user
# View a list of files available to you:

# ls
# View the contents of the send_message.py file:

# cat send_message.py
# Start sending messages to our DynamoDB table from our Messages SQS queue with an interval of 0.1 seconds:

# ./send_message.py -q Messages -i 0.1
# After a few seconds, hit Control + C to stop the command from continuing to run.

# Confirm Messages Were Inserted into the DynamoDB Table
# Return to the browser tab or window with the AWS console.
# In the search bar on top, enter "dynamodb".
# From the search results, select DynamoDB.
# In the left-hand navigation menu, select Tables.
# Select the Message table.
# In the top-right corner of the page, click Explore table itemsand review the list of items that were 
# inserted from our script, sent to SQS, triggered Lambda, and inserted into the DynamoDB database.
# Conclusion
# Congratulations — you've completed this hands-on lab!
#
    