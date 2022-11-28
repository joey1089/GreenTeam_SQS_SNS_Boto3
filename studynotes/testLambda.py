import boto3
import random
import string
import json


def lambda_handler(event, context):
    
    sqs = boto3.client('sqs')
    Rand_No_Str = (''.join(random.choices(string.ascii_letters+string.digits, k=10)))
    
    response = sqs.send_message(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/883139989797/MyProject-Week15-SQS-Queue',
        MessageBody=Rand_No_Str)
    
    print(response)   
    
    return {
        'statusCode': 200,
        'body': json.dumps(Rand_No_Str)
    }