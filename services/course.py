from uuid import uuid4
from schemas.course import CreateCourse, UpdateCoure, Course
from database import courses


class CourseServices:

    @staticmethod
    def all_course():
        return list(courses.values())

    @staticmethod
    def get_course_by_id(course_id: str):
        course = courses.get(str(course_id))
        if not course:
            return False
        return course

    @staticmethod
    def create_course(course_data: CreateCourse):
        for course in courses.values():
            if course.title == course_data.title:
                return False
        new_course = Course(course_id=str(uuid4()), **course_data.model_dump())
        courses[new_course.course_id] = new_course
        return new_course

    @staticmethod
    def update_course(course_id: str, course_data: UpdateCoure):
        course = courses.get(str(course_id))
        if not course:
            return None
        course.title = course_data.title
        course.description = course_data.description

        return course

    @staticmethod
    def delete_course(course_id: str):
        course = courses.get(str(course_id))
        if not course:
            return False
        del courses[course.course_id]
        return True

    @staticmethod
    def close_course(course_id: str):
        course = courses.get(str(course_id))
        if not course:
            return False
        course.is_open = False
        return True


course_services = CourseServices()
