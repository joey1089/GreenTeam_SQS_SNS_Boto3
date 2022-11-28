#To Create a SQS queue
import boto3
create_sqs_obj = boto3.client("sqs")

def create_sqs_queue(queue): #create a sqs queue and return the response
    try:
        response = create_sqs_obj.create_queue(
            QueueName=queue, # Name of the queue
            Attributes={
                "DelaySeconds": "0",        # No delays
                "VisibilityTimeout": "60",  # Gives a visibility time out of 60 seconds
            }
        )
    except:
        print(f"Unable to Create the {queue} queue at this time")
    print("Queue Url : ",queue.url)    
    return response

QUEUE_NAME = str(input("Enter the Name of your Queue : "))
print(create_sqs_queue(QUEUE_NAME))