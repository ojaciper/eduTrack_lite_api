from fastapi import APIRouter, HTTPException
from schemas.course import CreateCourse, UpdateCoure
from services.course import course_services
from database import courses

course_router = APIRouter()


@course_router.get("/all", status_code=200)
def course():
    course = course_services.all_course()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"msg": "success", "data": course}


@course_router.post("/create", status_code=204)
def create_course(course_data: CreateCourse):
    course = course_services.create_course(course_data)
    if not course:
        raise HTTPException(
            status_code=404, detail=f"Course already exist with thesame title"
        )
    return {"msg": "success", "data": course}


@course_router.get("/{course_id}", status_code=200)
def coure_by_id(course_id: str):
    course = course_services.get_course_by_id(course_id)
    if not course:
        raise HTTPException(status_code=200, detail="Course not found")
    return {"msg": "succces", "data": course}


@course_router.put("/update/{course_id}", status_code=200)
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


@course_router.get("/close/{course_id}", status_code=204)
def remove(course_id: str):
    course = course_services.close_course(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"msg": "success", "data": course}


