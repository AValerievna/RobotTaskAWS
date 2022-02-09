*** Settings ***
Test Template    Encryption test
Library          Libraries/S3HandlerLibrary.py    ${bucket_name}

*** Variables ***
${bucket_name}       drafts-s3-bucket

*** Test Cases ***
Encryption success    [Template]    Encryption test
    ServerSideEncryptionConfigurationNotFoundError    ${bucket_name}


*** Keywords ***
Encryption test    [Arguments]    ${error}    ${bucket_name}
    ${encryption}=    get bucket encryption    ${bucket_name}
    Should Not Contain    ${encryption}    ${error}


