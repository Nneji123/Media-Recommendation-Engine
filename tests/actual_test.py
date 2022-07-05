from fastapi.testclient import testclient
from .app import app

client = TestClient(app)

def test_movie():
    response = client.post("/movie")
    assert response.status_code == 200
    assert response.json() == 