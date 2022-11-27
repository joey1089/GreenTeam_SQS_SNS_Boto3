#Here we use Boto3's module method create_queue to create sqs messages 
import boto3
from botocore.exceptions import ClientError

create_sqs_obj = boto3.resource("sqs") # Create the SQS Object 

def create_queue(queue_name, delay_seconds, visiblity_timeout):
    """  Create a standard SQS queue   """
    try:
        response_obj = create_sqs_obj.create_queue(QueueName=queue_name,
                                             Attributes={
                                                 'DelaySeconds': delay_seconds,
                                                 'VisibilityTimeout': visiblity_timeout
                                             })
    except : #ClientError
        print(f'Unable to create SQS queue - {queue_name}.')
        # raise
    else:
        return response_obj



# Declare the constants that will not require its values changed
OUR_QUEUE_NAME = "Project-Week-15-Standard-Msg-QueueTest"
SECONDS_2_DELAY = "0"
TIMEOUT_4_QUE_VISIBLITY = "45"
output = create_queue(OUR_QUEUE_NAME, SECONDS_2_DELAY, TIMEOUT_4_QUE_VISIBLITY)
print(f'Std Msg Queue Name : {OUR_QUEUE_NAME} created. Queue URL - {output.url}')
