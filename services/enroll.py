from uuid import uuid4
from database import users, courses, enrollments
from schemas.enrollment import Enroll, CreateEnrollment, UpdateEnrollment


class EnrollmentService:
    @staticmethod
    def enroll(enroll_data: CreateEnrollment):
        user = users.get(str(enroll_data.user_id))
        course = courses.get(str(enroll_data.course_id))
        if not user:
            return "no_user"
        if not course:
            return "no_course"
        if not user.is_active:
            return "user_is_not_active"
        if not course.is_open:
            return "course_is_not_open"

        for enroll in enrollments.values():
            if enroll.course_id == enroll_data.course_id and user.id == enroll.user_id:
                return "course_already_enrolled"
        enroll_course = Enroll(id=str(uuid4()), **enroll_data.model_dump())
        enrollments[enroll_course.id] = enroll_course

        return enroll_course


enroll_services = EnrollmentService()
