from fastapi import FastAPI
from app.api import feedback, auth

app = FastAPI()

@app.get("/")
def root(): return {"message": "InsightHub backend is running"}

app.include_router(feedback.router)
app.include_router(auth.router)

