from fastapi import FastAPI 
 
from res.routes import base

app = FastAPI()
app.include_router(base.apiRouter)




 
