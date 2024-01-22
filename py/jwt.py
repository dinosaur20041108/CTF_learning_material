from hashlib import algorithms_available
import secrets
import jwt


payload={"user":"admin"}
secret="123456"
def jwt_encode(playload,secret):
    return jwt.encode(payload,secret,algorithm="HS256")

def jwt_decode(token,secret):
    return jwt.decode(payload,secret,algorithms=["HS256"])

token=jwt_encode(payload,secret)
print("token",token)
print(jwt_decode(token,secrets))