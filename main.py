from fastapi import FastAPI
from routes.user import user_router
from routes.course import course_router
from routes.enroll import course_enroll

app = FastAPI()





@app.get("/")
def home():
    return {"msg":"EduTrack lite api"}



app.include_router(user_router,prefix="/users", tags=["Users"])
app.include_router(course_router, prefix="/course", tags=["Course"])
app.include_router(course_enroll, prefix="/enroll",tags=["Course enrollment"])