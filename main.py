from fastapi import FastAPI,APIRouter,HTTPException
from .api.routers.city import city_router


app = FastAPI()

app.include_router(city_router)

@app.get("/health")
async def hello():
    return  {"API status":"Alive"}


