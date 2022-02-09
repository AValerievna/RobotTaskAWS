*** Settings ***
Test Template    Encryption test
Library          Libraries/S3HandlerLibrary.py    drafts-s3-bucket


*** Test Cases ***
Encryption success    [Template]    Encryption test
    ServerSideEncryptionConfigurationNotFoundError    drafts-s3-bucket


*** Keywords ***
Encryption test    [Arguments]    ${error}    ${bucket_name}
    ${encryption}=    get bucket encryption    ${bucket_name}
    Should Not Contain    ${encryption}    ${error}


