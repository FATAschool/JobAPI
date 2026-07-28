from sqlalchemy.orm import Mapped, mapped_column
from ..database.setup import (
    Base,
    engine,
    db
)
from sqlalchemy import String, Float
import uuid


class JobListing(Base):
    __tablename__ = "jobs"
    id:Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False)
    title:Mapped[str] = mapped_column(String(100), nullable=False)
    starting_salary:Mapped[float] = mapped_column(Float, default=0.00)
    requirement:Mapped[str] = mapped_column(String(500), nullable=True)
    qualification:Mapped[str] = mapped_column(String(250), nullable=True)
    company:Mapped[str] = mapped_column(String(200), nullable=False)


Base.metadata.create_all(bind=engine)


new_job = JobListing(
    title="Backend Junior Developer",
    starting_salary=2000,
    requirement="Proficient with python, 3+ years experience",
    qualification="",
    company="RtStudio"
)


db_session = db()
db_session.add(new_job)
db_session.commit()
db_session.refresh(new_job)
db_session.close()

print("{}".format(new_job.id))