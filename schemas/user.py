from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    user_id:str
    name:str
    email:str
    is_active:bool = True

class CreateUser(BaseModel):
    name:str
    email:str
    is_active:bool = True

class UpdateUser(BaseModel):
    name:Optional[str] = None
    email:Optional[str] = None
class DeactivateUser(BaseModel):
    is_active:bool = True