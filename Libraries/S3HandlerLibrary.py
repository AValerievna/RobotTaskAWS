from Project.s3_bucket_handler import S3BucketHandler


class S3HandlerLibrary(object):
    """
    library class for interaction of Robot Framework with S3-service
    """

    def __init__(self):
        self._handler = S3BucketHandler()
        self._res_resp = None

    def create_new_bucket(self, bucket_name, create_config):
        """
        create new bucket with bucket_name

        bucket_name: name of the new bucket
        create_config: CreateBucketConfiguration
        """
        self._handler.create_bucket(bucket_name, create_config)

    def encrypt_bucket(self, bucket_name, encrypt_config):
        """
        encrypt bucket with bucket_name

        bucket_name: name of the new bucket
        encrypt_config: ServerSideEncryptionConfiguration
        """
        self._handler.encrypt_bucket(bucket_name, encrypt_config)


    def delete_bucket(self, bucket_name):
        """
        delete bucket with bucket_name

        bucket_name: name of the new bucket
        """
        self._handler.delete_bucket(bucket_name)

    def get_bucket_encryption(self, bucket_name):
        """
        get bucket encryption

        bucket_name: name of the new bucket
        """
        return self._handler.get_bucket_encryption(bucket_name)

    def put_file(self, bucket_name, file_path, path_in_bucket):
        """
        put file in bucket

        bucket_name: name of the new bucket
        file_path: path of file to load
        path_in_bucket: path of file in bucket
        """
        self._handler.put_file(bucket_name, file_path, path_in_bucket)

    def get_bucket_objects(self, bucket_name):
        """
        get bucket objects list

        bucket_name: name of the new bucket
        """
        return self._handler.list_bucket_objects(bucket_name)

    def clear_bucket_objects(self, bucket_name):
        """
        clear all bucket objects

        bucket_name: name of the new bucket
        """
        self._handler.clear_bucket(bucket_name)

    def is_file_exist(self, bucket_name, path_in_bucket):
        """
        get if the file exist in bucket

        bucket_name: name of the new bucket
        path_in_bucket: path of file in bucket
        """
        return  self._handler.file_exist(bucket_name, path_in_bucket)

    def remove_bucket_file(self, bucket_name, path_in_bucket):
        """
        delete bucket in object with path_in_bucket

        bucket_name: name of the new bucket
        path_in_bucket: path to file in bucket
        """
        self._handler.remove_file(bucket_name, path_in_bucket)
