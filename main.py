from fastapi import FastAPI,APIRouter,HTTPException
from .api.routers.city import city_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(city_router)

@app.get("/health")
async def hello():
    return  {"API status":"Alive"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your frontend's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)