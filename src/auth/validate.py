from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from starlette import status

from src.auth.password_util import verify_password
from src.database import Session, connection
from src.signup.router import Attendees
security = HTTPBasic()


def validate_credentials(session: Annotated[Session, Depends(connection)] = ..., credentials: Annotated[HTTPBasicCredentials, Depends(security)] = ...,):
    attendee = session.query(Attendees).filter(Attendees.email == credentials.username).first()
    if not attendee or not verify_password(credentials.password, attendee.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
        )

    return True
