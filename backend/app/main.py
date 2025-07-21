from fastapi import FastAPI
from app.api import feedback

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "InsightHub backend is running"}

app.include_router(feedback.router)
