from sqlmodel import SQLModel, Field
from typing import Optional


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)
    hashed_password: str
    is_active: bool = True
    is_superuser: bool = False

    def verify_password(self, password: str) -> bool:
        from auth.password import verify_password
        return verify_password(password, self.hashed_password)


class UserPublic(SQLModel):
    id: int
    username: str
    email: str
    is_active: bool
    is_superuser: bool