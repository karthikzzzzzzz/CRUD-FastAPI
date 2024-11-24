

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from routers.token import verify_token

# OAuth2PasswordBearer is used to extract the token from the request headers
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_token(token, credentials_exception)
