from fastapi import FastAPI
from ...crud import (
    job
)

app = FastAPI()

    

@app.get("/api/v1")
def _get_api_v1():
    return {
        "message": "Hello this is the v1, for our open source project JobAPI"
    }
    
    
app.include_router(job.router)