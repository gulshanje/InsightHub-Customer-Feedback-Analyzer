from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.core.database import Base

class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String(100))
    message = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
