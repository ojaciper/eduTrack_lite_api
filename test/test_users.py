from fastapi import status


def test_list_users(client):
    res = client.get("/users/")
    assert res.status_code == status.HTTP_200_OK
    assert res.json()["msg"] == "success"
    assert isinstance(res.json()["data"], list)
    assert len(res.json()["data"]) >= 1


def test_get_user_by_id_success(client, any_user_id):
    res = client.get(f"/users/{any_user_id}")
    assert res.status_code == status.HTTP_200_OK
    assert res.json()["msg"]=="success"
    assert res.json()["data"]["user_id"] == any_user_id


def test_create_new_user(client):
     payload = {"name":"Tochi","email":"sophia@gmail.com", "is_active":True}
     res = client.post("/users/create", json=payload)
     assert res.status_code== status.HTTP_201_CREATED
     data = res.json()
     assert data['msg'] == "success"
     assert data["data"]["name"] == payload["name"]
     assert data["data"]["email"] == payload["email"]
     assert data["data"]["is_active"] == payload["is_active"]
   
         


def test_create_user_duplicate_email(client):
    res = client.get("/users/")
    existing_email = res.json()["data"][0]["email"]
    payload = {"name": "Peter", "email": existing_email, "is_active": True}
    resp = client.post("/users/create", json=payload)
    assert resp.status_code == status.HTTP_404_NOT_FOUND


def test_get_user_by_id_not_found(client, random_uuid):
    res = client.get(f"/users/{random_uuid}")
    assert res.status_code in [status.HTTP_200_OK, status.HTTP_404_NOT_FOUND]


def test_deactivate_user(client, any_user_id):
    res = client.get(f"users/deactivate/{any_user_id}")
    assert res.status_code in [status.HTTP_204_NO_CONTENT, status.HTTP_404_NOT_FOUND]
