from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from security import verify_password, create_token, hash_password

router = APIRouter(tags=["auth"])

FAKE_USER = {"username": "admin", "password_hash": hash_password("0000")}


@router.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends()):
    if form.username != FAKE_USER["username"]:
        raise HTTPException(status_code=400, detail="Usuario incorrecto")

    if not verify_password(form.password, FAKE_USER["password_hash"]):
        raise HTTPException(status_code=400, detail="Password incorrecto")

    token = create_token(form.username)
    return {"access_token": token, "token_type": "bearer"}
