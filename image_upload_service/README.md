# README for Image Upload Service
This README entails everything that is needed to run this service.  
To use this service, POST to /upload/ in multi-part form-data.

Key for data is
* user_id
* access_token
* image

## Third Party Dependencies
* Django
* Requests
* boto3

## Environment Variables
* BASE_URL
* BUCKET_NAME
* AWS_ACCESS_KEY_ID
* AWS_SECRET_ACCESS_KEY

## Components
* parser
* uploader
* put

### Parser
Parse the data from POST request

### Uploader
Call boto3 and AWS API to put the image file into s3 bucket.
Returns the URL that can be used to access the image

### Put
Update the user information in the data endpoint
