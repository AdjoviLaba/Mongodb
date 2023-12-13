import uuid
from typing import Optional
from pydantic import BaseModel, Field

class Person(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    last_name: str = Field(...)
    adress: str = Field(...)
    phone: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "name": "Don Quixote",
                "last_name": "Miguel de Cervantes",
                "adress": "...",
                "phone": "336-567-9094"
            }
        }


class PersonUpdate(BaseModel):
    name: Optional[str]
    last_name: Optional[str]
    adress: Optional[str]
    phone: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "name": "Don Quixote",
                "last_name": "Miguel de Cervantes",
                "adress": "...",
                "phone": "336-567-9094"
            }
        }
