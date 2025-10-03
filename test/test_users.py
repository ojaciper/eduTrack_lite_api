from fastapi.testclient import TestClient
from main import app
from fastapi import status

client = TestClient(app)

def test_all_user():
    response = client.get("/users/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['msg'] == 'success'
   