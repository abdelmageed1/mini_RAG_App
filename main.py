from fastapi import FastAPI 
 
from res.routes import base , data

app = FastAPI()
app.include_router(base.apiRouter)
app.include_router(data.dataRouter)




 
