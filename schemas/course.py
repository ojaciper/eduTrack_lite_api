from pydantic import BaseModel


class Course(BaseModel):
    course_id: str
    title: str
    description: str
    is_open: bool = True


class CreateCourse(BaseModel):
    title: str
    description: str
    is_open:bool = True

class UpdateCoure(BaseModel):
    title:str
    description:str
