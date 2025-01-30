from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the University API!"}

def test_create_student():
    response = client.post("/students/1", json={"name": "John Doe"})
    assert response.status_code == 200
    assert response.json() == {"student_id": 1, "name": "John Doe"}

def test_read_student():
    response = client.get("/students/1")
    assert response.status_code == 200
    assert response.json() == {"student_id": 1, "name": "John Doe"} 