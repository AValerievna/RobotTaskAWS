*** Settings ***
Test Template     Encryption test
Library           ../Libraries/s3_handler_library.py


*** Test Cases ***
Encryption success [Template] Encryption test
    ServerSideEncryptionConfigurationNotFoundError  s3_test_bucket


*** Keywords ***
Encryption test [Arguments] ${error} ${bucket_name}
    ${encryption} = get bucket encryption ${bucket_name}
    should not contain value ${encryption} ${error}


