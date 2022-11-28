import boto3
import datetime
import json

def lambda_handler(event, context):
    
    sqs = boto3.client('sqs')
    str_current_time = str(datetime.datetime.now()) # Not implemented yet
    # Rand_No_Str = (''.join(random.choices(string.ascii_letters+string.digits, k=10)))
    #print("\n Current Time : ",str_current_time.strftime('%H:%M:%S on %A, %B the %dth, %Y')) 
    # utctime = str(datetime.datetime.utcnow())
    # print(utctime)

    # response = sqs.send_message(
    #     QueueUrl='https://sqs.us-east-1.amazonaws.com/ReplacewithCloud_user/MyProject-Week15-SQS-Queue',
    #     MessageBody=str_current_time)
    
    # print(response)  
   
    
    return {
        'statusCode': 200,
        'body': json.dumps(str_current_time)
    }

lambda_handler(event=1, context=2)