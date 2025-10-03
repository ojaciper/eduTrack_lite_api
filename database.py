from schemas.user import User
from schemas.course import Course
from schemas.enrollment import Enroll
from uuid import uuid4

users: dict[str, User] = {}
courses: dict[str, Course] = {}
enrollments: dict[str, Enroll] = {}


user_data = [
    {"name": "Peter osas", "email": "osaspeter@gmail.com", "is_active": True},
    {"name": "Victor Jumbo", "email": "jumbovictor@gmail.com", "is_active": True},
    {"name": "Destiny Paul", "email": "pauldestiny@gmail.com", "is_active": True},
    {"name": "David Nice", "email": "david@gmail.com", "is_active": True},
]
course_data = [
    {"title":"Introduction to Python-fastapi", "description":"Fast-api is python web framework use to build restful api","is_open":True},
    {"title":"Mastering Flutter", "description":"Flutter crossplatform framework use to build mobile app","is_open":True},
    {"title":"Mastering Python language", "description":"Python is one of the language powering ai model","is_open":True},
    {"title":"Introduction to to golang", "description":"How to build restful api using go","is_open":True}
]

for user in user_data:
    user_data = User(user_id=str(uuid4()), **user)
    users[user_data.user_id] = user_data
    
for course in course_data:
    course_data = Course(course_id=str(uuid4()), **course)
    courses[course_data.course_id] = course_data
