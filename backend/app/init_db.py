from core.database import engine
from app.models.feedback import Feedback
from app.models.user import User 
from core.database import Base

def init():
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created.")

if __name__ == "__main__":
    init()
