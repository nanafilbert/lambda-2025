import json
import boto3

def lambda_handler(event, context):
    """
    AWS Lambda function handler
    """
    try:
        # Log the incoming event
        print(f"Received event: {json.dumps(event)}")
        
        # Example processing
        message = event.get('message', 'Hello from Lambda!')
        
        # Example AWS service interaction
        # s3 = boto3.client('s3')
        # buckets = s3.list_buckets()
        
        response = {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'message': message,
                'timestamp': context.aws_request_id,
                'function_name': context.function_name
            })
        }
        
        return response
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }