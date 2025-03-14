from fastapi import APIRouter, HTTPException
from models.user import UserCreate
from config.db import user_collection
import bcrypt

user_router = APIRouter(prefix="/user", tags=["user"])

@user_router.post("/register")
async def register_view(user_client : UserCreate):
    
    try:
        
        user_on_db = user_collection.find_one({"email":user_client.email})

        if user_on_db:
            raise HTTPException(detail="Email in use.", status_code=400)
        
        user_client.password = bcrypt.hashpw(user_client.password.encode("utf-8"), bcrypt.gensalt())

        id_user_created = user_collection.insert_one(user_client.__dict__).inserted_id

        user_created = user_collection.find_one({"_id":id_user_created})
        
        if not user_created:
            raise HTTPException(detail="User not created", status_code=400)

        del user_created["_id"]
    
    except:
        raise HTTPException(detail="User not created.", status_code=400)

    return user_created