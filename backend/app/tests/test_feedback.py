from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_feedback():
    response = client.post("/feedback", json={
        "customer_name": "Test User",
        "message": "Test message"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["customer_name"] == "Test User"
    assert data["message"] == "Test message"
    assert "id" in data

def test_get_feedback():
    response = client.get("/feedback")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if data:
        assert "message" in data[0]
