import time
import jwt 
from decouple import config 

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

def token_respone(token:str):
    return {
        "access_token" : token
    }

def signJWT(userID: str):
    payload = {
        "userID":userID,
        "expiry": time.time()+600
    }

    token=jwt.encode(payload,JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_respone(token)

def decodeJWT(token:str):
    try:
        decode_token=jwt.decode(token, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return decode_token if decode_token["expires"]>=time.time() else None
    except:
        return {}