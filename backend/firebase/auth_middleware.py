
from fastapi import Header, HTTPException
from firebase_admin import auth

def firebase_auth(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing token")
    token = authorization.split(" ")[1]
    return auth.verify_id_token(token)

def admin_only(user):
    if not user.get("admin", False):
        raise HTTPException(status_code=403, detail="Admin access required")
