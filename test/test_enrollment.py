from fastapi import status
from datetime import datetime


def test_all_enrollment_empty(client):
    res = client.get("/enroll/")
    assert res.status_code == status.HTTP_200_OK
    assert res.json()["msg"] == "success"
    assert isinstance(res.json()["data"],list)
    
    
def test_enroll_course(client, any_course_id, any_user_id):
    payload = {
        "user_id": any_user_id,
        "course_id": any_course_id,
        "enrolled_date": datetime.now().isoformat(),
        "completed": False,
    }
    res = client.post("/enroll/course/enroll", json=payload)
    assert res.status_code in [status.HTTP_201_CREATED, status.HTTP_404_NOT_FOUND]
   
    
def test_user_enrolled_courses(client,any_user_id):
    res = client.get(f"/enroll/course/{any_user_id}")
    assert res.status_code in [ status.HTTP_200_OK, status.HTTP_404_NOT_FOUND]
    # assert res.json()["msg"] == 'success'
    # assert isinstance(res.json()["data"], list)
    