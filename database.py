import os
from collections.abc import Generator
from pathlib import Path
from dotenv import load_dotenv
from sqlmodel import Session, create_engine

# Load .env, or the existing .env.file name used by this project.
env_dir = Path(__file__).resolve().parent
env_path = env_dir / ".env"
if not env_path.exists():
    env_path = env_dir / ".env.file"
load_dotenv(dotenv_path=env_path)

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:YOUR_PASSWORD_HERE@localhost:5432/neuroteach_db",
)

# SQLModel database engine
engine = create_engine(DATABASE_URL, echo=False)


def get_session() -> Generator[Session, None, None]:
    """FastAPI dependency that yields a database session per request."""
    with Session(engine) as session:
        yield session