from fastapi import APIRouter, HTTPException
from schemas.user import CreateUser, UpdateUser
from services.user import user_services
from database import users


user_router = APIRouter()


@user_router.get("/", status_code=200)
def user():
    user = user_services.all_user()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {"msg": "success", "data": user}


@user_router.get("/{user_id}", status_code=200)
def user_by_id(user_id: str):
    user = user_services.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"msg": "success", "data": user}


@user_router.post("/create", status_code=201)
def user(user_data: CreateUser):
    user = user_services.create_user(user_data)
    if not user:
        raise HTTPException(status_code=409, detail="User aready exist")
    return {"msg": "success", "data": user}


@user_router.put("/update/{user_id}", status_code=200)
def user_update(user_id: str, user_data: UpdateUser):
    user = user_services.update_user(user_id, user_data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"msg": "success", "data": user}


@user_router.delete("/remove/{user_id}", status_code=204)
def remove_user(user_id):
    user = user_services.delete_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"msg": "success"}


@user_router.get("/deactivate/{user_id}", status_code=204)
def deactivate(user_id: str):
    user = user_services.deactivate_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
