def test_server_running(client):
    # arrange
    ENDPOINT = "/"
    EXPECTED_ROOT_TEXT = b"<h1>Not Found</h1>"

    # act
    response = client.get(ENDPOINT)

    # assert
    assert EXPECTED_ROOT_TEXT in response.data
    assert response.status_code == 404
