import logging

import boto3
from botocore.exceptions import ClientError

from config import AWS_SERVER_PUBLIC_KEY, AWS_SERVER_SECRET_KEY


class S3BucketHandler(object):

    def __init__(self, public_key=AWS_SERVER_PUBLIC_KEY, secret_key=AWS_SERVER_SECRET_KEY):
        self._s3_client = boto3.client('s3', aws_access_key_id=public_key, aws_secret_access_key=secret_key)
        self._s3_resource = boto3.resource('s3', aws_access_key_id=public_key, aws_secret_access_key=secret_key)


    def create_bucket(self, bucket_name, create_config):
        try:
            self._s3_resource.meta.client.head_bucket(Bucket=bucket_name)
        except ClientError:
            self._s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=create_config)
            logging.info(f"Bucket {bucket_name} created successfully")


    def encrypt_bucket(self, bucket_name, encrypt_config):
        self._s3_client.put_bucket_encryption(Bucket=bucket_name, ServerSideEncryptionConfiguration=encrypt_config)
        logging.info(f"Bucket {bucket_name} was encrypted")

    def delete_bucket(self, bucket_name):
        self._s3_client.delete_bucket(Bucket=bucket_name)
        logging.info(f"Bucket {bucket_name} was deleted")

    def get_bucket_encryption(self, bucket_name):
        try:
            enc = self._s3_client.get_bucket_encryption(Bucket=bucket_name)
            rules = enc['ServerSideEncryptionConfiguration']['Rules']
            logging.info('Bucket: %s, Encryption: %s' % (bucket_name, rules))
            return rules
        except ClientError as e:
            if e.response['Error']['Code'] == 'ServerSideEncryptionConfigurationNotFoundError':
                logging.error("Bucket: %s, no server-side encryption" % bucket_name)
            else:
                logging.error("Bucket: %s, unexpected error: %s" % (bucket_name, e))
            return e.response['Error']['Code']

    def put_file(self, bucket_name, file_path, path_in_bucket):
        with open(file_path, 'rb') as data:
            self._s3_client.upload_fileobj(data, bucket_name, path_in_bucket)

    def list_bucket_objects(self, bucket_name):
        bucket = self._s3_resource.Bucket(bucket_name)
        return [bucket_object.key for bucket_object in bucket.objects.all()]

    def file_exist(self, bucket_name, path_in_bucket):
        try:
            self._s3_client.head_object(Bucket=bucket_name, Key=path_in_bucket)
            return True
        except ClientError as e:
            logging.error("Bucket: %s, unexpected error: %s" % (bucket_name, e))
            return False

    def clear_bucket(self, bucket_name):
        bucket = self._s3_resource.Bucket(bucket_name)
        bucket.objects.all().delete()

    def remove_file(self, bucket_name, path_in_bucket):
        self._s3_resource.Object(bucket_name, path_in_bucket).delete()
