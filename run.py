import uvicorn
"""
This module, scaffolds the manual way to run this project
manually you would do this "uvicorn app.api.v1.application:app --reload --host 0.0.0.0 --port 8001"
simply type on the cmd "python3 run.py", to run this file
it will run the whole fastAPI project at an instance
"""


if __name__ == "__main__":
    uvicorn.run("app.api.v1.application:app", host="0.0.0.0", port=8001, reload=True)