from pydantic import BaseModel, Field, EmailStr

class UserSchema(BaseModel):
    fullname: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)
    class Config:
        the_extra = {
            "user_demo":{
                "fullname":"abc",
                "email":"abc@g.com",
                "password":"12345"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)
    class Config:
        the_extra = {
            "user_demo":{
                "email":"abc@g.com",
                "password":"12345"
            }
        }