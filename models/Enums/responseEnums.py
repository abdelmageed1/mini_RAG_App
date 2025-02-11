from enum import Enum


class ResponseResult(Enum):
    FILE_TYPE_NOT_SUPPORTED = "this extention not allowed"
    FILE_SIZE_EXCEEDED = "the size is exceeded"
    FILE_UPLOADED_SUCCSSES = "Success Upload"
    FILE_UPLOAD_SUCCESS = "file_upload_success"
    FILE_UPLOAD_FAILED = "file_upload_failed"