from . import client


def test_root_url(client):
    response = client.get("/")
    assert response.status_code == 404
    assert response.json == {"description": "Not Found"}
