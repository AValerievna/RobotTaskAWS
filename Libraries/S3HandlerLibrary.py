from Project.s3_bucket_handler import S3BucketHandler


class S3HandlerLibrary(object):
    """
    library class for interaction of Robot Framework with S3-service
    """

    def __init__(self, bucket_name):
        self._api_worker = S3BucketHandler(bucket_name)
        self._res_resp = None

    def create_new_bucket(self, bucket_name):
        """
        create new bucket with bucket_name

        bucket_name: name of the new bucket
        """
        self._res_resp = self._api_worker.create_bucket(bucket_name)

    def list_buckets(self):
        """
        list all S3 buckets
        """
        self._res_resp = self._api_worker.list_buckets()

    def get_bucket_encryption(self, bucket_name):
        """
        get bucket encryption

        bucket_name: name of the new bucket
        """
        return self._api_worker.get_bucket_encryption(bucket_name)

    def put_file(self, file_path, bucket_name):
        """
        put file in bucket

        file_path: path of file to load
        bucket_name: name of the new bucket
        """
        return self._api_worker.put_file(file_path, bucket_name)
