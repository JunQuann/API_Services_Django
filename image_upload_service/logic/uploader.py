import boto3
import os

s3 = boto3.resource('s3')
bucket_name = os.environ.get('BUCKET_NAME')
bucket = s3.Bucket(bucket_name)
region_name = s3.meta.client.get_bucket_location(Bucket=bucket_name)["LocationConstraint"]

def upload(image, key):
    bucket.put_object(Body=image.read(), Key=key, ContentType='image/png')
    url = "http://s3-{region}.amazonaws.com/{bucket}/{key}".format(region=region_name, bucket=bucket_name, key=key)
    return url
