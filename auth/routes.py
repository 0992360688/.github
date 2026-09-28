from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session

from auth.dependencies import get_current_user
from auth.password import hash_password, verify_password
from auth.roles import get_user_role
from auth.tokens import Token, create_token
from database import get_session
from models.user import User, UserPublic

router = APIRouter()


class SignupRequest(BaseModel):
    username: str = Field(min_length=1, max_length=64)
    email: str = Field(min_length=3, max_length=320)
    password: str = Field(min_length=8)


class LoginRequest(BaseModel):
    username: str
    password: str


@router.post("/signup", response_model=UserPublic)
def signup(payload: SignupRequest, session: Session = Depends(get_session)) -> UserPublic:
    new_user = User(
        username=payload.username,
        email=payload.email,
        hashed_password=hash_password(payload.password),
    )
    session.add(new_user)
    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username or email is already registered",
        ) from None
    session.refresh(new_user)
    return new_user


@router.post("/login", response_model=Token)
def login(payload: LoginRequest, session: Session = Depends(get_session)) -> Token:
    user = session.query(User).filter(User.username == payload.username).first()
    if not user or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = create_token(data={"sub": user.username})
    return Token(access_token=token, token_type="bearer")


@router.get("/users/me", response_model=UserPublic)
def read_users_me(current_user: User = Depends(get_current_user)) -> User:
    return current_user


@router.get("/users/me/role")
def read_user_role(current_user: User = Depends(get_current_user)) -> dict[str, str]:
    role = get_user_role(current_user)
    return {"role": role}