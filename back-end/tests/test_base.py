def test_server_running(client):
    response = client.get("/")

    assert b"<h1>Not Found</h1>" in response.data
    assert response.status_code == 404
