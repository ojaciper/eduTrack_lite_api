from pydantic import BaseModel
from datetime import datetime


class Enroll(BaseModel):
    id:str
    user_id:str
    course_id:str
    enrolled_date:datetime
    completed:bool = False

class CreateEnrollment(BaseModel):
    user_id:str
    course_id:str
    enrolled_date:datetime
    completed:bool= False

class UpdateEnrollment(BaseModel):
    user_id:str
    course_id:str
    enrolled_date:datetime

class UpdateCompleted(BaseModel):
    completed:bool=False