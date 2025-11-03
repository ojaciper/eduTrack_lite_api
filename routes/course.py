from fastapi import APIRouter, HTTPException
from schemas.course import CreateCourse, IsOpen, UpdateCoure
from services.course import course_services
from database import courses

course_router = APIRouter()


@course_router.get("", status_code=200)
def course():
    course = course_services.all_course()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"msg": "success", "data": course}


@course_router.post("", status_code=201)
def create_course(course_data: CreateCourse):
    course = course_services.create_course(course_data)
    if not course:
        raise HTTPException(
            status_code=404, detail=f"Course already exist with thesame title"
        )
    return {"msg": "success", "data": course}


@course_router.get("{course_id}", status_code=200)
def coure_by_id(course_id: str):
    course = course_services.get_course_by_id(course_id)
    if not course:
        raise HTTPException(status_code=200, detail="Course not found")
    return {"msg": "success", "data": course}


@course_router.put("/{course_id}", status_code=200)
def update_course(course_id: str, course_data: UpdateCoure):
    course = course_services.update_course(course_id, course_data)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"msg": "success", "data": course}


@course_router.delete("/{course_id}", status_code=204)
def remove(course_id: str):
    course = course_services.delete_course(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"msg": "success", "data": course}


@course_router.patch("/{course_id}/close", status_code=204)
def remove(course_id: str, isopen:IsOpen):
    course = course_services.close_course(course_id, isopen)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"msg": "success", "data": course}


@course_router.get("/users/{course_id}/enrollment", status_code=200, tags=None)
def user_course_enrollment(course_id: str):
    course = course_services.users_enrrolled_in_course(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="course not found")
    if course == False:
        raise HTTPException(status_code=404, detail="no user enroll on this course")
    return course
