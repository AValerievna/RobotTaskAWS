import logging

import boto3
from botocore.exceptions import ClientError

from config import AWS_SERVER_PUBLIC_KEY, AWS_SERVER_SECRET_KEY


class S3BucketHandler(object):

    def __init__(self, bucket_name
                 , public_key=AWS_SERVER_PUBLIC_KEY, secret_key=AWS_SERVER_SECRET_KEY
    ):
        self._s3_client = boto3.client('s3',
                                       aws_access_key_id=public_key, aws_secret_access_key=secret_key
                                       )
        self._s3_resource = boto3.resource('s3',
                                           aws_access_key_id=public_key, aws_secret_access_key=secret_key
                                           )
        self._s3_bucket_name = bucket_name
        try:
            self._s3_resource.meta.client.head_bucket(Bucket=bucket_name)
        except ClientError:
            self._s3_client.create_bucket(Bucket=bucket_name,
                                          CreateBucketConfiguration ={'LocationConstraint': 'eu-central-1'})
            logging.info(f"Bucket {bucket_name} created successfully")

        response = self._s3_client.put_bucket_encryption(
            Bucket=bucket_name,
            ServerSideEncryptionConfiguration={
                'Rules': [{'ApplyServerSideEncryptionByDefault': {'SSEAlgorithm': 'AES256'}}]})
        logging.info(f"Bucket {bucket_name} was encrypted")


    def create_bucket(self, bucket_name, config):
        self._s3_client.create_bucket(Bucket=bucket_name,
                                      CreateBucketConfiguration=config
                                      )
        logging.info(f"Bucket {bucket_name} created successfully")

    def list_buckets(self):
        return self._s3_client.list_buckets()

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

    def put_file(self, file_path, bucket_name):
        # Read the file stored on your local machine
        with open(file_path, 'rb') as data:
            # Upload the file ATA.txt within the Myfolder on S3
            self._s3_client.upload_fileobj(data, bucket_name, file_path)

    # def get(self, src, dst):
    #     try:
    #         container = self._s3_resource.Bucket(self._s3_bucket_name)
    #         for obj in container.objects.filter(Prefix=src):
    #             dst_path = os.path.join(dst, obj.key)
    #             mkpath(os.path.dirname(dst_path))
    #             container.download_file(obj.key, dst_path)
    #     except:
    #         return False
    #     else:
    #         return True
    #
    # def put(self, src: str, dst: str = None) -> bool:
    #     try:
    #         if os.path.isdir(src):
    #             names = os.listdir(src)
    #         else:
    #             names = [src]
    #         for n in names:
    #             src_name = os.path.join(src, n)
    #             dst_name = os.path.join(dst, n)
    #
    #             if os.path.isdir(src_name):
    #                 if not self.put(src_name, dst_name):
    #                     raise S3FileUploadError
    #             else:
    #                 logging.debug('s3 put: %s -> %s' % (src_name, dst_name))
    #                 try:
    #                     self.client.head_object(Bucket=self.bucket, Key=dst_name)
    #                 except:
    #                     self.client.upload_file(src_name, self.bucket, dst_name, ExtraArgs={'ACL': 'public-read-write'})
    #     except Exception as e:
    #         logging.error(str(e), exc_info=True)
    #         return False
    #     else:
    #         return True
