from res.helpers.config import getSetting ,Settings
from fastapi import UploadFile
from .BaseController import BaseController 
from .ProjectController import ProjectController
from  res.models.Enums.responseEnums import ResponseResult
import re , os

class DataController(BaseController):
    
    def __init__(self):
        super().__init__()
        self.size_scale = 1048576 # convert MB to bytes    

    
    def validate_upload_file(self ,file:UploadFile)    :

        if file.content_type not in self.app_setting.FILE_ALLOWED_UPLOAD :
            return False , ResponseResult.FILE_TYPE_NOT_SUPPORTED.value
        
        if file.size > self.app_setting.FILE_MAX_LENGHT * self.size_scale:
            return False  , ResponseResult.FILE_SIZE_EXCEEDED.value
        
        return True  , ResponseResult.FILE_UPLOADED_SUCCSSES.value

    def generate_unique_filepath(self, orig_file_name: str, project_id: str):

        random_key = self.generate_random_string()
        project_path = ProjectController().get_project_path(project_id=project_id)

        cleaned_file_name = self.get_clean_file_name(
            orig_file_name=orig_file_name
        )

        new_file_path = os.path.join(
            project_path,
            random_key + "_" + cleaned_file_name
        )

        while os.path.exists(new_file_path):
            random_key = self.generate_random_string()
            new_file_path = os.path.join(
                project_path,
                random_key + "_" + cleaned_file_name
            )

        return new_file_path, random_key + "_" + cleaned_file_name

    def get_clean_file_name(self, orig_file_name: str):

        # remove any special characters, except underscore and .
        cleaned_file_name = re.sub(r'[^\w.]', '', orig_file_name.strip())

        # replace spaces with underscore
        cleaned_file_name = cleaned_file_name.replace(" ", "_")

        return cleaned_file_name

