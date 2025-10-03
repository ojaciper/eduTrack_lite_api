from fastapi import status
 
def test_list_all_courses(client):
    res = client.get("/course/all")
    assert res.status_code == status.HTTP_200_OK
    assert res.json()["msg"] == "success"
    assert isinstance(res.json()["data"], list)
    assert len(res.json()["data"]) >=1
    
def test_get_course_by_id_success(client, any_course_id):
    res = client.get(f"/course/{any_course_id}")
    assert res.status_code == status.HTTP_200_OK
    assert res.json()["msg"] == "success"