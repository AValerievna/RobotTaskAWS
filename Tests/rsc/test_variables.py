bucket_name = "drafts-s3-bucket"
encrypt_config = {'Rules': [{'ApplyServerSideEncryptionByDefault': {'SSEAlgorithm': 'AES256'}}]}
create_config = {'LocationConstraint': 'eu-central-1'}
no_encryption_error="ServerSideEncryptionConfigurationNotFoundError"
file_path="Tests/rsc/test_txt_file.txt"
path_in_bucket="loaded_test_file.txt"