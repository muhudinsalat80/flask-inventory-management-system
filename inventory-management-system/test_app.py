from app import app

client = app.test_client()

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_inventory():
    response = client.get("/inventory")
    assert response.status_code == 200