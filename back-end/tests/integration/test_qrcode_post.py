from pathlib import Path 


# get the resources folder in the tests folder
RESOURCES = Path(__file__).parent.parent / "resources"

def test_qrcode_1(client):
    # arrange
    ENDPOINT = "/qrcode"
    DATA = {"url": "https://unamur.be"}
    EXPECTED_QRCODE = RESOURCES / "qrcode_unamur.png"

    # act
    response = client.post(ENDPOINT, json=DATA)

    # assert
    assert response.status_code == 200
    assert open(EXPECTED_QRCODE, "rb").read() == response.data

def test_qrcode_2(client):
    # arrange
    ENDPOINT = "/qrcode"
    DATA = {"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}
    EXPECTED_QRCODE = RESOURCES / "qrcode_suspicious.png"

    # act
    response = client.post(ENDPOINT, json=DATA)

    # assert
    assert response.status_code == 200
    assert response.data == open(EXPECTED_QRCODE, "rb").read()
