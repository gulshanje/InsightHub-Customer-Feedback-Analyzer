from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class FeedbackCreate(BaseModel):
    customer_name: Optional[str] = "Anonymous"
    message: str

class FeedbackResponse(BaseModel):
    id: int
    customer_name: str
    message: str
    created_at: datetime

    class Config:
        from_attributes = True
