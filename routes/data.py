from fastapi import FastAPI , APIRouter ,Depends , UploadFile , status
from fastapi.responses import JSONResponse

import os 

from res.helpers.config import getSetting ,Settings
from res.controllers.DataController import DataController

dataRouter = APIRouter(
    prefix="/api/v1/data",
    tags=['api_v1','data']
)

@dataRouter.post('/upload/{project_id}')
async def load_data(project_id :str, file :UploadFile , 
                    app_setting :Settings =Depends(getSetting) 
                    ):
    
    is_valid , result = DataController().validate_upload_file(file=file)
     
    return {
        "message" : result ,
        'is_valid' : is_valid
    }