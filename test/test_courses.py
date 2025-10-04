from fastapi import status


def test_list_all_courses(client):
    res = client.get("/course/all")
    assert res.status_code == status.HTTP_200_OK
    assert res.json()["msg"] == "success"
    assert isinstance(res.json()["data"], list)
    assert len(res.json()["data"]) >= 1


def test_create_course(client):
    payload = {"title": "Introduction to html", "description": "just the basice", "is_open": True}
    res = client.post("/course/create", json=payload)
    assert res.status_code == status.HTTP_201_CREATED
    data = res.json()
    assert data["msg"] == "success"
    assert data["data"]["title"] == payload["title"]
    assert data["data"]["description"] == payload["description"]
    assert data["data"]["is_open"] == payload["is_open"]  
    
    


def test_get_course_by_id_success(client, any_course_id):
    res = client.get(f"/course/{any_course_id}")
    assert res.status_code == status.HTTP_200_OK
    assert res.json()["msg"] == "success"
    assert res.json()["data"]["course_id"] == any_course_id


def test_get_user_by_id_not_found(client, random_uuid):
    res = client.get(f"/course/{random_uuid}")
    assert res.status_code in [status.HTTP_200_OK, status.HTTP_404_NOT_FOUND]


def test_create_course_duplicate_title(client):
    courses = client.get("/course/all").json()["data"]
    existing_title = courses[0]["title"]
    payload = {
        "title": existing_title,
        "description": "any description",
        "is_open": True,
    }
    res = client.post("/course/create", json=payload)
    assert res.status_code in [status.HTTP_204_NO_CONTENT, status.HTTP_404_NOT_FOUND]


def test_close_course(client, any_course_id):
    res = client.get(f"/course/close/{any_course_id}")
    assert res.status_code in [status.HTTP_204_NO_CONTENT, status.HTTP_200_OK]
