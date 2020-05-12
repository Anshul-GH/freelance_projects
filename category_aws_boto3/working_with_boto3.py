import boto3
import uuid

# to connect to low-level client interface, we use client()
s3_client = boto3.client('s3')

# to connect to high-level interface, we use resources
s3_resource = boto3.resource('s3')

# creating a bucket
def create_bucket_name(bucket_prefix):
    # the generated bucket name must be 3 and 63 characters long
    return ''.join([bucket_prefix, str(uuid.uuid4())])


def create_new_bucket(bucket_prefix, s3_connection):
    session = boto3.session.Session()
    current_region = session.region_name
    bucket_name = create_bucket_name(bucket_prefix)
    bucket_response= s3_connection.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': current_region
        })

    # print(bucket_name, current_region)
    return bucket_name, bucket_response

"""
OUTPUT:
firstautobucket4b36ee5a-9858-4369-b781-57db5a850a71 ap-south-1
firstautobucket4b36ee5a-9858-4369-b781-57db5a850a71
{'ResponseMetadata': {'RequestId': '01527786FEEE1AE4', 'HostId': '08PCv7sVlhUfJe9CoWsqr10nLTKzzYZv60pIjh2zfYGbSIz7+HzNSLgKO1N9IS69hqnzG81sPBI=', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amz-id-2': '08PCv7sVlhUfJe9CoWsqr10nLTKzzYZv60pIjh2zfYGbSIz7+HzNSLgKO1N9IS69hqnzG81sPBI=', 'x-amz-request-id': '01527786FEEE1AE4', 'date': 'Tue, 12 May 2020 18:29:33 GMT', 'location': 'http://firstautobucket4b36ee5a-9858-4369-b781-57db5a850a71.s3.amazonaws.com/', 'content-length': '0', 'server': 'AmazonS3'}, 'RetryAttempts': 0}, 'Location': 'http://firstautobucket4b36ee5a-9858-4369-b781-57db5a850a71.s3.amazonaws.com/'}

firstautobucket01c34117-1084-4385-a74a-a210acf9f045 ap-south-1
{'ResponseMetadata': {'RequestId': '20D82F58E5A6572A', 'HostId': 'aUAavPYhU7YUt0RUvqVG7DaDnYIHsMUZG2O48CchLTcylZXPvXlio0SB4UdtZy/PtIUu1cflvzY=', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amz-id-2': 'aUAavPYhU7YUt0RUvqVG7DaDnYIHsMUZG2O48CchLTcylZXPvXlio0SB4UdtZy/PtIUu1cflvzY=', 'x-amz-request-id': '20D82F58E5A6572A', 'date': 'Tue, 12 May 2020 19:56:53 GMT', 'location': 'http://firstautobucket01c34117-1084-4385-a74a-a210acf9f045.s3.amazonaws.com/', 'content-length': '0', 'server': 'AmazonS3'}, 'RetryAttempts': 0}, 'Location': 'http://firstautobucket01c34117-1084-4385-a74a-a210acf9f045.s3.amazonaws.com/'}
"""

# creates a random file with a random prefix to avoid partition clogging for aws s3
def create_temp_file(size, file_name, file_content):
    random_file_name = ''.join([str(uuid.uuid4().hex[:6], file_name])
    with open(random_file_name, 'w') as f:
        f.write(str(file_content) * size)
    
    return random_file_name



if __name__ == "__main__":
    first_bucket_name, first_response = create_new_bucket(
        bucket_prefix='firstautobucket',
        s3_connection=s3_resource.meta.client
        )
    
    # print(first_bucket_name)
    # print(first_response)

    first_file_name = create_temp_file(300, 'firstfile.txt', 'f')

    # creating bucket and object instance
    first_bucket = s3_resource.Bucket(name=first_bucket_name)
    first_object = s3_resource.Object(
        bucket_name=first_bucket_name, key=first_file_name
    )

    # alternatively for object
    first_object_again = first_bucket.Object(first_file_name)
    first_object_again = first_object.Bucket()


    # Uploading the file to s3

    # Option 1: Object instance version
    s3_resource.Object(first_bucket_name, first_file_name).upload_file(
        Filename=first_file_name)
    # or
    first_object.upload_file(first_file_name)

    # Option 2: Bucket instance version
    s3_resource.Bucket(first_bucket_name).upload_file(
        Filename=first_file_name, Key=first_file_name
    )

    # Option 3: Client version
    s3_resource.meta.client.upload_file(
        Filename=first_file_name, Bucket=first_bucket_name,
        Key=first_file_name
    )



    # Downloading a file from S3
    s3_resource.Object(first_bucket_name, first_file_name).download_file(
        f'/tmp/{first_file_name}')



