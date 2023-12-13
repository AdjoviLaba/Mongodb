from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, schema):
        return {"type": "string"}

class PersonModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    name: str
    last_name: str
    address: str
    tel: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
        schema_extra = {
            "example": {
                "name": "John",
                "last_name": "Doe",
                "address": "123 Main St",
                "tel": "123-456-7890"
            }
        }
