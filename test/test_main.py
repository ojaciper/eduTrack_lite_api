from fastapi import status


def test_home(client):
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"msg":"EduTrack lite api"}
                    