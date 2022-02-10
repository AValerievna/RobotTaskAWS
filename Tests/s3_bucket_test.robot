*** Settings ***
Suite Setup      Create encrypted bucket    ${bucket_name}  ${create_config}  ${encrypt_config}
Suite Teardown   Remove bucket    ${bucket_name}
Library          Libraries/S3HandlerLibrary.py
Variables        Tests/rsc/test_variables.py


*** Test Cases ***
Encryption success    [Template]    Encryption test
    ${bucket_name}    ${no_encryption_error}

File upload success    [Template]    Upload file test
    ${bucket_name}     ${file_path}    ${path_in_bucket}



*** Keywords ***
Encryption test    [Arguments]    ${bucket_name}    ${error}
    ${encryption}=    get bucket encryption    ${bucket_name}
    Should Not Contain    ${encryption}    ${error}

Create encrypted bucket     [Arguments]    ${bucket_name}   ${create_config}  ${encrypt_config}
    create new bucket    ${bucket_name}   ${create_config}
    encrypt bucket    ${bucket_name}   ${encrypt_config}

Upload file test    [Arguments]    ${bucket_name}   ${file_path}   ${path_in_bucket}
    ${res} =   put file    ${bucket_name}   ${file_path}   ${path_in_bucket}
    ${bucket_objects} =   get bucket objects    ${bucket_name}
    Should Contain    ${bucket_objects}   ${path_in_bucket}
    [Teardown]    remove bucket file     ${bucket_name}    ${path_in_bucket}

Remove bucket    [Arguments]    ${bucket_name}
    delete bucket    ${bucket_name}
