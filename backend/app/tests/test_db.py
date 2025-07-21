from sqlalchemy import text
from app.core.database import SessionLocal

def test_database_connection():
    db = SessionLocal()
    try:
        db.execute(text("SELECT 1"))
        assert True
    except Exception as e:
        assert False, f"Database connection failed: {e}"
    finally:
        db.close()
