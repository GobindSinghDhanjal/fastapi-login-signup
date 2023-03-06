import uvicorn
from fastapi import FastAPI, Body
from app.model import UserSchema, UserLoginSchema
from app.auth.jwt_handler import signJWT

users = []

app = FastAPI()

@app.get("/", tags=["test"])
def greet():
    return {"Hello":"World!"}

@app.post("/user/signup", tags=["user"])
def user_signup(user: UserSchema = Body(default=None)):
    users.append(user)
    return signJWT(user.email)

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False

@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {"error":"Invalid login details"}