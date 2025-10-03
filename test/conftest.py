import pytest
from fastapi.testclient import TestClient
from main import app
from database import users, courses, enrollments
from schemas.user import User, CreateUser
from schemas.course import Course, CreateCourse
from schemas.enrollment import Enroll, CreateEnrollment
from datetime import datetime
from uuid import uuid4

@pytest.fixture
def client():
    """Create a test client for the FastAPI app"""
    return TestClient(app)

@pytest.fixture
def sample_user_data():
    """Sample user data for testing"""
    return {
        "name": "Test User",
        "email": "test@example.com",
        "is_active": True
    }

@pytest.fixture
def sample_course_data():
    """Sample course data for testing"""
    return {
        "title": "Test Course",
        "description": "A test course for unit testing",
        "is_open": True
    }

@pytest.fixture
def test_user():
    """Create a test user in the database"""
    user_id = str(uuid4())
    user = User(
        user_id=user_id,
        name="Test User",
        email="testuser@example.com",
        is_active=True
    )
    users[user_id] = user
    return user

@pytest.fixture
def test_course():
    """Create a test course in the database"""
    course_id = str(uuid4())
    course = Course(
        course_id=course_id,
        title="Test Course",
        description="A test course",
        is_open=True
    )
    courses[course_id] = course
    return course

@pytest.fixture
def test_enrollment(test_user, test_course):
    """Create a test enrollment in the database"""
    enrollment_id = str(uuid4())
    enrollment = Enroll(
        id=enrollment_id,
        user_id=test_user.user_id,
        course_id=test_course.course_id,
        enrolled_date=datetime.now(),
        completed=False
    )
    enrollments[enrollment_id] = enrollment
    return enrollment

@pytest.fixture(autouse=True)
def cleanup_database():
    """Clean up the database before each test"""
    # Store original data
    original_users = users.copy()
    original_courses = courses.copy()
    original_enrollments = enrollments.copy()
    
    yield
    
    # Restore original data after test
    users.clear()
    users.update(original_users)
    courses.clear()
    courses.update(original_courses)
    enrollments.clear()
    enrollments.update(original_enrollments)
