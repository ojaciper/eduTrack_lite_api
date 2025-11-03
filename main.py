from fastapi import FastAPI, Request
from routes.user import user_router
from routes.course import course_router
from routes.enroll import course_enroll
import logging
app = FastAPI(title="EduTrack Lite API")



# @app.middleware("http")
# async def log_request(request:Request, call_next):
#     logging.info(f'Incoming request:{request.method} {request.url}')
#     response = await call_next(request)
#     logging.info(f'Request status: {response.status_code}')
#     return response

# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s = %(levelname)s - %(message)s",
#     filename='app.log',
#     filemode="a"
# )


@app.get("/home", tags={"Home"})
def home():
    logging.info("Root endpoint accessed")
    return {"msg":"EduTrack lite api"}



app.include_router(user_router,prefix="/users", tags=["User"])
app.include_router(course_router, prefix="/course", tags=["Course"])
app.include_router(course_enroll, tags=["Course enrollment"])
