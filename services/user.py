from uuid import uuid4
from schemas.user import User, CreateUser, UpdateUser
from database import users


class UserServices:

    @staticmethod
    def all_user():
        return list(users.values())
    
    @staticmethod
    def get_user_by_id(user_id:str):
        user = users.get(str(user_id))
        if not user:
            return False
        return user
    
    
    @staticmethod
    def create_user(user_data: CreateUser):
        for user in users.values():
            if user.email == user_data.email:
                return False
        new_user = User(user_id=str(uuid4()), **user_data.model_dump())
        users[new_user.id] = new_user
        return new_user

    @staticmethod
    def update_user(user_id:str,user_date:UpdateUser):
        user = users.get(str(user_id))
        if not user:
            return None
        user.name = user_date.name
        user.email = user_date.email
        return user
        

    @staticmethod
    def delete_user(user_id:str):
        user = users.get(str(user_id))
        if not user:
            return False
        del users[user.id]
        return True

    @staticmethod
    def deactivate_user(user_id:str):
        user = users.get(str(user_id))
        if not user:
            return False
        user.is_active = False
        return True



user_services = UserServices()
