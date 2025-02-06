from fastapi import FastAPI , APIRouter ,Depends , UploadFile
import os 
from res.helpers.config import getSetting ,Settings
from res.controllers.DataController import DataController

dataRouter = APIRouter(
    prefix="/api/v1/data",
    tags=['api_v1','data']
)

@dataRouter.post('/upload/{project_id}')
async def load_data(project_id :str, file :UploadFile , 
                    pp_setting :Settings =Depends(getSetting) 
                    ):
    
    is_valid , result = DataController().validate_upload_file(file=file)
    
    return {
        "message" : result ,
        'is_valid' : is_valid
    }