from typing import Generator
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal


def get_db() -> Generator[Session, None, None]:
    """
    FastAPI dependency that yields a database session per request
    and guarantees the session is closed once the request is complete.
    """
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
