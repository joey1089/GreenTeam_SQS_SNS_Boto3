#To Create a SQS queue
import boto3
create_sqs_obj = boto3.client("sqs") # we are using boto3.client than resource here,so it returns dict

def create_sqs_queue(queue_name): #create a sqs queue and return the response
    ''' This method require queue name(str) as an arguement,
      this method prints out the queue url and also returns the response if no error found. '''
    try:
        response = create_sqs_obj.create_queue( #response gets the actual response from the created sqs object
            QueueName=queue_name, # Name of the queue
            Attributes={
                "DelaySeconds": "0",        # No delays
                "VisibilityTimeout": "60",  # Gives a visibility time out of 60 seconds
            }
        )
    except:
        print(f"Unable to Create the {queue_name} queue at this time")
    print("\n Queue Url : ", response['QueueUrl'],"\n") 
    return response

QUEUE_NAME = "MyProject-Week15-SQS-Queue"
print(create_sqs_queue(QUEUE_NAME))