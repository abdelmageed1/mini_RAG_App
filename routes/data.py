from fastapi import FastAPI , APIRouter ,Depends , UploadFile , status
from fastapi.responses import JSONResponse
import aiofiles

import os 
from res.models.Enums.responseEnums import  ResponseResult
from res.helpers.config import getSetting ,Settings
# from res.controllers import DataController,  
import logging
from .schemes.data import ProcessRequset
from res.controllers import DataController ,ProjectController, ProcessController

logger = logging.getLogger('uvicorn.error')
dataRouter = APIRouter(
    prefix="/api/v1/data",
    tags=['api_v1','data']
)

 


@dataRouter.post('/upload/{project_id}')
async def load_data(project_id :str, file :UploadFile , 
                    app_setting :Settings =Depends(getSetting) 
                    ):
        # validate the file properties
    data_controller = DataController()
   
    is_valid , result = data_controller.validate_upload_file(file=file)
     
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": result
            }
        )
    
    project_dir_path = ProjectController().get_project_path(project_id=project_id)
    file_path, file_id = data_controller.generate_unique_filepath(
        orig_file_name=file.filename,
        project_id=project_id
    )

    try:
        async with aiofiles.open(file_path, "wb") as f:
            while chunk := await file.read(Settings.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:

        logger.error(f"Error while uploading file: {e}")

        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": ResponseResult.FILE_UPLOAD_FAILED.value
            }
        )

    return JSONResponse(
            content={
                "signal": ResponseResult.FILE_UPLOAD_SUCCESS.value,
                "file_id": file_id
            }
        )


@dataRouter.post('/process/{project_id}')
async def process_data(project_id :str, request :ProcessRequset):
    file_id = request.file_id
    chunk_size = request.chunk_size
    overlap_size = request.chunk_overlap

    process_controller = ProcessController(prject_id=project_id)

    file_content = process_controller.get_file_content(file_id=file_id)

    file_chunks = process_controller.process_file_content(
        file_content=file_content,
        file_id=file_id,
        chunk_size=chunk_size,
        overlap_size=overlap_size
    )

    if file_chunks is None or len(file_chunks) == 0:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": ResponseResult.PROCESSING_FAILED.value
            }
        )

    return file_chunks