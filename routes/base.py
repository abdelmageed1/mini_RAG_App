from fastapi import FastAPI , APIRouter
import os 
 

apiRouter = APIRouter(
    prefix="/api/v1",
    tags=['api_v1']
)

@apiRouter.get("/")
async def welcome():
     app_name = os.getenv('APP_NAME')
     app_version = os.getenv("APP_VERSION")

     return {
         "app_name": app_name,
        "app_version": app_version,
         }


 
 