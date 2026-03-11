
def test_status_ok(client):
    resp, _ = client.get("/", params={"name": "michael"})
    assert resp is not None
    assert resp.status_code == 200

def test_json_format(client):
    resp, _ = client.get("/", params={"name": "michael"})
    assert resp.headers.get("Content-Type", "").startswith("application/json")

def test_schema_fields(client):
    resp, _ = client.get("/", params={"name": "michael"})
    data = resp.json()
    for field in ["name", "age", "count"]:
        assert field in data

def test_types(client):
    resp, _ = client.get("/", params={"name": "michael"})
    data = resp.json()
    assert isinstance(data["name"], str)
    assert isinstance(data["count"], int)
    assert isinstance(data["age"], (int, type(None)))

def test_invalid_input_empty_name(client):
    resp, _ = client.get("/", params={"name": ""})
    assert resp.status_code == 200
    data = resp.json()
    assert "name" in data

def test_numeric_name(client):
    resp, _ = client.get("/", params={"name": "123"})
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data["name"], str)
