from app import create_app


def test_create_and_list():
    client = create_app().test_client()
    assert client.post("/api/attendance", json={"name": "Unit"}).status_code == 201
    assert client.get("/api/attendance").json[0]["name"] == "Unit"
