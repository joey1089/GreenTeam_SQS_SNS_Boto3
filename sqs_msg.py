#To Create a SQS queue
import boto3

def create_sqs_queue(): #create a sqs queue and return the response
    create_sqs_obj = boto3.client("sqs")
    response = create_sqs_obj.create_queue(
        QueueName="Project-Week15-Std-Msg-Queue", # Name of the queue
        Attributes={
            "DelaySeconds": "0",        # No delays
            "VisibilityTimeout": "60",  # Gives a visibility time out of 60 seconds
        }
    )
    return response

print(create_sqs_queue())

#In case if you want to delete the queue 
# refer https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html#SQS.Client.delete_queue
