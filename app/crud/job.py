# from ..models import (
#     testModel
# )
from fastapi import status, APIRouter
from ..database.setup import (
    Base,
    db,
    engine
)

# def init_db():
#     Base.metadata.create_all(bind=engine)
#     db_session = db()

router = APIRouter(prefix="/api/v1")

@router.post("/new-job/", status_code=status.HTTP_201_CREATED)
async def _add_new_job(request):
    print(request)
    return {
        "success": 200,
        "data": request,
    }