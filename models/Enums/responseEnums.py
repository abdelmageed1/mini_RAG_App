from enum import Enum


class ResponseResult(Enum):
    FILE_TYPE_NOT_SUPPORTED = "this extention not allowed"
    FILE_SIZE_EXCEEDED = "the size is exceeded"
    FILE_UPLOADED_SUCCSSES = "Success Upload"