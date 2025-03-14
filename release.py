import boto3
import os

# Fetch credentials from environment variables
aws_access_key = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_region = os.getenv('AWS_REGION', 'us-east-1')  # Default to 'us-east-1' if not set

# Initialize the S3 client using environment variables
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region
)

print('Uploading macOS installer to S3. This may take a while...')

BUCKET_NAME = 'fibula-femr-installer'

s3.upload_file(
    f'./test.txt', 
    BUCKET_NAME, 
    f'test.txt'
)