from fastapi import FastAPI , APIRouter # type: ignore
import os 
from res.helpers.config import getSetting
 

apiRouter = APIRouter(
    prefix="/api/v1",
    tags=['api_v1']
)

@apiRouter.get("/")
async def welcome():
     
     app_setting = getSetting()

     app_name = app_setting.APP_NAME 
     app_version = app_setting.APP_VERSION

     return {
         "app_name": app_name,
        "app_version": app_version,
         }


 
 