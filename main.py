from fastapi import FastAPI
from routes.user import user_router
from routes.course import course_router

app = FastAPI()


app.include_router(user_router,prefix="/users", tags=["Users"])
app.include_router(course_router, prefix="/course", tags=["Course"])


@app.get("/")
def home():
    return {"message":"EduTrack lite api"}