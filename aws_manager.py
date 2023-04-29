import boto3
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
from botocore.client import Config
from botocore.exceptions import ClientError
import json

# local file imports
import main
import hash_calc


class FileDownloadError(Exception):
    """returns 4XX error code if file not downloaded"""


def download_file_from_s3(bucket_name, object_key, download_path):
    try:
        s3_object = S3.Object(bucket_name, object_key)
        s3_object.download_file(download_path)
        return s3_object.metadata
    except ClientError as error:
        if 400 <= error.response['ResponseMetadata']['HTTPStatusCode'] < 500:
            raise FileDownloadError(error)
        else:
            raise


def object_tagging(bucket_name, object_key, result):
    response = client.put_object_tagging(
        Bucket=bucket_name,
        Key=object_key,
        Tagging={
            'TagSet': [
                {
                    'Key': 'Detect',
                    'Value': result,
                },
            ],
        },
    )
    # print(response)


# setting clients for boto library to connect with AWS, here default creds are used from aws/credentials
# Force a retry after 3 seconds rather than 60
S3 = boto3.resource('s3', config=Config(connect_timeout=3, read_timeout=3, retries={'max_attempts': 2}), verify=False)
client = boto3.client('s3', verify=False)

bucket = 'mohit-test'   # bucket name
remote_file = 'clean.xlsx'      # object name to be scanned
local_path = 'payloads/' + str(remote_file)     # local file path where fine should be stored

try:
    # below are all S3 operations
    file_metadata = download_file_from_s3(bucket, remote_file, local_path)  # download file and get its metadata
    sha256, md5 = hash_calc.compute_hashes(local_path)      # calculate file hashes
    print("SHA256: " + str(sha256) + "\nMD5: " + str(md5))
    result = main.one_by_one(local_path)     # scan file using analyser in main file
    print(result)
    object_tagging(bucket, remote_file, result)      # tag file with results on bucket

except Exception as e:
    print(e)
