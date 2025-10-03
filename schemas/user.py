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
    name:str
    email:str