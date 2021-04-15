import boto3
import requests

s3 = boto3.client('s3')


# ACCESS_KEY= "my_accesss_key_id"
# SECRET_KEY= "my_secret_access_key"


# s3 = boto3.client('s3',
#     aws_access_key_id=ACCESS_KEY,
#     aws_secret_access_key=SECRET_KEY
# )

# specify your bucket name in which you are gonna upload file
bucket = "my-bucket"

# s3 bucket path wiht file name
remote_file_path = "test/test2.xlsx"


# Generating pre-signed url...
url = s3.generate_presigned_url('put_object', Params={'Bucket':bucket,'Key':remote_file_path}, ExpiresIn=3600, HttpMethod='PUT')

print("Response", url)

# read a file which needs to be uploaded
file_path = "/home/girish/Downloads/col-oriented.xlsx"
with open(file_path, 'rb') as f:
    data =f.read()
    http_response = requests.put(url, data=data)


# If successful, returns HTTP status code 204
print(f'File upload HTTP status code: {http_response.status_code}')


'''
========================================================================================


params can be:

ACL, Body, Bucket, CacheControl, ContentDisposition, ContentEncoding, ContentLanguage, ContentLength, ContentMD5, ContentType,
 Expires, GrantFullControl, GrantRead, GrantReadACP, GrantWriteACP, Key, Metadata, ServerSideEncryption, StorageClass, WebsiteRedirectLocation,
  SSECustomerAlgorithm, SSECustomerKey, SSECustomerKeyMD5, SSEKMSKeyId, SSEKMSEncryptionContext, BucketKeyEnabled, RequestPayer, Tagging, 
  ObjectLockMode, ObjectLockRetainUntilDate, ObjectLockLegalHoldStatus, ExpectedBucketOwner


generate_presigned_url(ClientMethod, Params=None, ExpiresIn=3600, HttpMethod=None) method of botocore.client.S3 instance
    Generate a presigned url given a client, its method, and arguments
    
    :type ClientMethod: string
    :param ClientMethod: The client method to presign for
    
    :type Params: dict
    :param Params: The parameters normally passed to
        ``ClientMethod``.
    
    :type ExpiresIn: int
    :param ExpiresIn: The number of seconds the presigned url is valid
        for. By default it expires in an hour (3600 seconds)
    
    :type HttpMethod: string
    :param HttpMethod: The http method to use on the generated url. By
        default, the http method is whatever is used in the method's model.
    
    :returns: The presigned url
==============================================================================================
'''
