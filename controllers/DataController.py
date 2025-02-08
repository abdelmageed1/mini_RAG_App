from res.helpers.config import getSetting ,Settings
from fastapi import UploadFile
from .BaseController import BaseController
from  res.models.Enums.responseEnums import ResponseResult


class DataController(BaseController):
    
    def __init__(self):
        super().__init__()
        self.size_scale = 1048576 # convert MB to bytes    

    
    def validate_upload_file(self ,file:UploadFile)    :

        if file.content_type not in self.app_setting.FILE_ALLOWED_UPLOAD :
            return False , ResponseResult.FILE_TYPE_NOT_SUPPORTED
        
        if file.size > self.app_setting.FILE_MAX_LENGHT * self.size_scale:
            return False  , ResponseResult.FILE_SIZE_EXCEEDED
        
        return True  , ResponseResult.FILE_UPLOADED_SUCCSSES

   
