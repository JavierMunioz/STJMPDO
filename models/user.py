from pydantic import BaseModel

class UserBasic(BaseModel):
    username : str
    email : str
    rol : str


class UserCreate(UserBasic):
    password : str


class UserResponse(UserBasic):
    _id : str

