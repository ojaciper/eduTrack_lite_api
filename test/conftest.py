import pytest
from main import app
from fastapi.testclient import TestClient
from database import users, courses
from schemas.user import User
from uuid import uuid4
from datetime import datetime


@pytest.fixture(scope="session")
def any_user_id():
    return next(iter(users.keys()))


@pytest.fixture(scope="session")
def any_course_id():
    return next(iter(courses.keys()))


@pytest.fixture(scope="session")
def random_uuid():
    return str(uuid4())


@pytest.fixture()
def client():
    return TestClient(app)


@pytest.fixture(scope="session")
def enroll_course_payload():
    payload = {
        "user_id": any_user_id,
        "course_id": any_course_id,
        "enrolled_date": datetime.now().isoformat(),
        "completed": False,
    }
    return payload
