def test_server_running(client):
    # arrange
    ROOT_TEXT = b"<h1>Not Found</h1>"

    # act
    response = client.get("/")

    # assert
    assert ROOT_TEXT in response.data
    assert response.status_code == 404
