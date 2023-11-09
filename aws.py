import boto3

s3_client = boto3.client('s3')
response = s3_client.list_buckets()

print("S3 Buckets:")
for bucket in response['Buckets']:
    print(f" - {bucket['Name']}")
    print(f"   Created: {bucket['CreationDate']}")
    print()

