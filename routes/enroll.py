from fastapi import APIRouter, HTTPException
from schemas.enrollment import CreateEnrollment
from services.enroll import enroll_services


course_enroll = APIRouter()


@course_enroll.post("/course/enroll", status_code=201)
def enroll_course(enroll_data: CreateEnrollment):
    course_enroll = enroll_services.enroll(enroll_data)
    if course_enroll == "course_not_open":
        raise HTTPException(status_code=404, detail="Course is close for enrollment")

    if course_enroll == "course_already_enrolled":
        raise HTTPException(
            status_code=409, detail="you can't enroll twice on this course"
        )
    if course_enroll == "no_user":
        raise HTTPException(status_code=404, detail="User not found")
    if course_enroll == "no_course":
        raise HTTPException(status_code=404, detail="Course not found")
    
    if course_enroll == "user_is_not_active":
        raise HTTPException(status_code=401, detail="User not active")

    return {"msg": "success", "data": course_enroll}


@course_enroll.get("/course/{user_id}", status_code=200)
def user_enrolled_course(user_id: str):
    enrolled = enroll_services.user_course_enrolled(user_id)
    if not  enrolled:
        raise HTTPException(status_code=404, detail="user not found")
    return {"msg": "success", "data": enrolled}


@course_enroll.get("enrollment/course/{enrollment_id}/completed", status_code=204)
def course_completed(enrollment_id: str):
    enrolled = enroll_services.course_completed(enrollment_id)
    if not enrolled:
        raise HTTPException(status_code=404, detail="Course enrollment nof found")
    return {"msg": "success"}


@course_enroll.get("/", status_code=200)
def all_course_enrolled():
    enrolled = enroll_services.all_enrollment()
    if not enrolled:
        raise HTTPException(status_code=404, detail ="Course not found")
    return {"msg": "success", "data": enrolled}
