from fastapi import FastAPI,APIRouter
base_routers = APIRouter(
prefix="/base",
tags=["base"]
)
@base_routers.get("/")
def welcome():   
     return {"Hello": "World"}

#uvicorn main:app --reload --host 0.0.0.0 --port 5000  where main is the name of the file and app is the name of the FastAPI instance.


