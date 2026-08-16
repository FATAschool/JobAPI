import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./jobapi.db")

# SQLite requires 'check_same_thread': False for FastAPI multi-threading
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args,
    echo=os.getenv("SQL_ECHO", "False").lower() in ("true", "1", "t"),
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
