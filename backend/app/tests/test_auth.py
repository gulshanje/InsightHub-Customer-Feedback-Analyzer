from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_and_auth_flow():
    user = {"username": "demo", "email": "demo@mail.com", "password": "123456"}
    client.post("/auth/register", json=user)

    res = client.post("/auth/login", data={"username": "demo", "password": "123456"})
    assert res.status_code == 200
    token = res.json()["access_token"]

    headers = {"Authorization": f"Bearer {token}"}
    res = client.get("/auth/me", headers=headers)
    assert res.status_code == 200
    assert res.json()["username"] == "demo"
