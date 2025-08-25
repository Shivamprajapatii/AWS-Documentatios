import json
import boto3
from datetime import datetime

# Initialize S3 client
s3 = boto3.client('s3')

# Replace with your bucket name
BUCKET_NAME = "my-iot-device-bucket"

def lambda_handler(event, context):
    """
    AWS Lambda function to store IoT messages in S3 with organized folders
    """
    try:
        # IoT message payload
        if 'payload' in event:
            payload = event['payload']
            # If payload is base64 encoded, decode it
            if isinstance(payload, str):
                message = json.loads(payload)
            else:
                message = payload
        else:
            message = event
    
        # Extract deviceId and timestamp
        device_id = message.get('deviceId', 'UnknownDevice')
        timestamp = message.get('timestamp')  # Expecting ISO8601 string

        # Parse timestamp to datetime object
        if timestamp:
            dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
        else:
            dt = datetime.utcnow()

        year = dt.strftime('%Y')
        month = dt.strftime('%m')
        day = dt.strftime('%d')
        ts = int(dt.timestamp() * 1000)  # Milliseconds

        # Build S3 key
        s3_key = f"test-device/{year}/{month}/{day}/{device_id}/{ts}.json"

        # Convert message to JSON string
        json_data = json.dumps(message)

        # Upload to S3
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=s3_key,
            Body=json_data,
            ContentType='application/json'
        )

        return {
            "statusCode": 200,
            "body": f"Message stored in {s3_key}"
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": str(e)
        }
