# eduTrack_lite

A lightweight FastAPI service for managing users, courses, and enrollments.

## Requirements
- Python 3.10+
- pip

## Setup
```bash
# 1) Clone and enter the project
git clone https://github.com/ojaciper/eduTrack_lite_api.git
cd eduTrack_lite

# 2) Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# 3) Install dependencies
pip install -r requirements.txt
```

## Run (development)
The FastAPI app is defined in `main.py` as `app`.
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

API docs:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Project structure
```
.
├─ main.py
├─ database.py
├─ routes/
│  ├─ user.py
│  ├─ course.py
│  └─ enroll.py
├─ schemas/
│  ├─ user.py
│  ├─ course.py
│  └─ enrollment.py
├─ services/
│  ├─ user.py
│  ├─ course.py
│  └─ enroll.py
├─ test/
│  ├─ conftest.py
│  ├─ test_main.py
│  ├─ test_users.py
│  ├─ test_courses.py
│  └─ test_enrollment.py
└─ requirements.txt
```


## Testing
Run the test suite with pytest:
```bash
python -m pytest -v
```