from fastapi import FastAPI , APIRouter

apiRouter = APIRouter()

@apiRouter.get("/")
def welcome():
    return {
        "message": "Hello World!"
    }