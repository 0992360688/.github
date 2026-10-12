from typing import Optional
from sqlmodel import Field, SQLModel


class ChallengeBase(SQLModel):
    sub_module_id: int = Field(foreign_key="sub_modules.id", index=True, nullable=False)
    title: str = Field(min_length=1, max_length=200)
    xp_reward: int = Field(default=50, ge=0)


class Challenge(ChallengeBase, table=True):
    __tablename__ = "challenges"

    id: Optional[int] = Field(default=None, primary_key=True)


class ChallengeCreate(ChallengeBase):
    pass


class ChallengeRead(ChallengeBase):
    id: int
