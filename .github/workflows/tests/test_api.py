import requests

API_URL = "https://api.quotable.io/random"

def test_status_code():
    response = requests.get(API_URL, timeout=5)
    assert response.status_code == 200

def test_json_structure():
    response = requests.get(API_URL, timeout=5)
    data = response.json()
    assert "content" in data
    assert "author" in data
    assert isinstance(data["content"], str)
    assert isinstance(data["author"], str)

def test_latency_under_1s():
    response = requests.get(API_URL, timeout=5)
    assert response.elapsed.total_seconds() < 1


