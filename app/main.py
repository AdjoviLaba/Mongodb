from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from route import router as person_router

config = dotenv_values(".env")

app = FastAPI()

async def startup_event():
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]

async def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(person_router, tags=["persons"], prefix="/person")