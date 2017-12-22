import boto3
import botocore

s3 = boto3.resource('s3')
bucket_name = 'interwovn-mvp'
bucket = s3.Bucket(bucket_name)

def upload(image, user_id):
    bucket.upload_fileobj(image, str(user_id))
