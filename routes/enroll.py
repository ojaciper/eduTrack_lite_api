from fastapi import APIRouter, HTTPException
from schemas.enrollment import CreateEnrollment
from services.enroll import enroll_services


course_enroll = APIRouter()


@course_enroll.post("/course/enroll", status_code=200)
def enroll_course(enroll_data: CreateEnrollment):
    course_enroll = enroll_services.enroll(enroll_data)
    if course_enroll == "course_is_not_open":
        raise HTTPException(status_code=404, detail="Course is close for enrollment")
    if course_enroll == "course_already_enrolled":
        raise HTTPException(
            status_code=404, detail="you can't enroll twic on this course"
        )
    if course_enroll == " no_user":
        raise HTTPException(status_code=404, detail="User not found")
    if course_enroll == " no_course":
        raise HTTPException(status_code=404, detail="Course not found")

    return {"msg": "success", "data": course_enroll}
