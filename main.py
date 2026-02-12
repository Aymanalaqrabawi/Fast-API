from fastapi import FastAPI
from routes import base
app = FastAPI()
app.include_router(base.base_routers)
@app.get("/")
def read_root():   
     return {"Hello": "World"}

#uvicorn main:app --reload --host 0.0.0.0 --port 5000  where main is the name of the file and app is the name of the FastAPI instance.

