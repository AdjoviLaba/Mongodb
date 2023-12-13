from fastapi import FastAPI
from models import PersonModel
from database import db  # Assuming you have a database.py for MongoDB connection

app = FastAPI()

@app.post("/persons/", response_model=PersonModel)
async def create_person(person: PersonModel):
    person_dict = person.model_dump(by_alias=True)
    result = await db["persons"].insert_one(person_dict)
    new_person = await db["persons"].find_one({"_id": result.inserted_id})
    return new_person
