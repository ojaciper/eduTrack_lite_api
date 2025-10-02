from schemas.user import User
from schemas.course import Course
from schemas.enrollment import Enroll

users:dict[str, User] = {}
courses:dict[str,Course] = {}
enrollments:dict[str,Enroll] ={}