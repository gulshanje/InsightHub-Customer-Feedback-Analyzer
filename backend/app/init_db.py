from core.database import engine
from models.feedback import Feedback
from core.database import Base

def init():
    Base.metadata.create_all(bind=engine)
    print("✅ Database tables created.")

if __name__ == "__main__":
    init()
