from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models import Person, PersonUpdate

router = APIRouter()

@router.post("/", response_description="Create a new Person", status_code=status.HTTP_201_CREATED, response_model=Person)
def create_person(request: Request, person: Person = Body(...)):
    person = jsonable_encoder(person)
    new_person = request.app.database["persons"].insert_one(person)
    created_person = request.app.database["persons"].find_one(
        {"_id": new_person.inserted_id}
    )

    return created_person


@router.get("/", response_description="Person List", response_model=List[Person])
def list_person(request: Request):
    person = list(request.app.database["persons"].find(limit=100))
    return person


@router.get("/{id}", response_description="Get a single person by id", response_model=Person)
def find_person(id: str, request: Request):
    if (person := request.app.database["persons"].find_one({"_id": id})) is not None:
        return person

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Person with ID {id} not found")


@router.put("/{id}", response_description="Update a Person", response_model=Person)
def update_person(id: str, request: Request, person: PersonUpdate = Body(...)):
    person = {k: v for k, v in person.dict().items() if v is not None}

    if len(person) >= 1:
        update_result = request.app.database["persons"].update_one(
            {"_id": id}, {"$set": person}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Person with ID {id} not found")

    if (
        existing_person := request.app.database["Persons"].find_one({"_id": id})
    ) is not None:
        return existing_person

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Person with ID {id} not found")


@router.delete("/{id}", response_description="Delete a Person")
def delete_person(id: str, request: Request, response: Response):
    delete_result = request.app.database["persons"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Person with ID {id} not found")
