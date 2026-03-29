from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_home():
    res = client.get("/")
    assert res.status_code == 200

def test_add():
    res = client.get("/add/3/4")
    assert res.json()["result"] == 7

