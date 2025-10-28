from uuid import uuid4
from database import users, courses, enrollments
from schemas.enrollment import Enroll, CreateEnrollment, UpdateEnrollment


class EnrollmentService:
    @staticmethod
    def enroll(enroll_data: CreateEnrollment):
        user = users.get(str(enroll_data.user_id))
        course = courses.get(str(enroll_data.course_id))
        if not course:
            return "no_course"
        if not user:
            return "no_user"
        if not course.is_open == True:
            return "course_not_open"
        if not user.is_active:
            return "user_is_not_active"

        for enroll in enrollments.values():
            if (
                enroll.course_id == enroll_data.course_id
                and user.user_id == enroll.user_id
            ):
                return "course_already_enrolled"
        enroll_course = Enroll(id=str(uuid4()), **enroll_data.model_dump())
        enrollments[enroll_course.id] = enroll_course

        return enroll_course

    @staticmethod
    def course_completed(id: str):
        course_enrolled = enrollments.get(str(id))
        if not course_enrolled:
            return False
        course_enrolled.completed = False
        return True

    @staticmethod
    def all_enrollment():
        enrolleds = list(enrollments.values())
        if len(enrolleds) <= 0:
            return None
        return enrolleds

    @staticmethod
    def user_course_enrolled(user_id: str):
        user = users.get(str(user_id))
        if not user:
            return None
        enrolleds = []
        for enrolled in enrollments.values():
            if enrolled.user_id == user_id:
                enrolleds.append(enrolled)
        return enrolleds

    @staticmethod
    def get_all_user_courese(user_id: str):
        user = users.get(str(user_id))
        if not user:
            return None
        user_course = []
        for en in enrollments.values():
            if en.user_id == user_id:
                for cu in courses.values():
                    if en.course_id == cu.course_id:
                        user_course.append(cu)
        return user_course


enroll_services = EnrollmentService()
