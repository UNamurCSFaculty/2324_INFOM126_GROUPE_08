from datetime import datetime
from api.models import Message
from api.database import db
from api.controllers import guest_book_POST


def test_guestbook_1(client):
    # arrange
    ENDPOINT = "/guest-book"
    EXPECTED_JSON = {"entries": []}

    # act
    response = client.get(ENDPOINT)

    # assert
    assert response.status_code == 200
    assert response.json == EXPECTED_JSON


def test_guestbook_2(client):
    # arrange
    ENDPOINT = "/guest-book"
    AUTHOR = "Jean"
    TEXT = "Bonjour,"
    
    # act
    with client.application.app_context():
        guest_book_POST(AUTHOR, TEXT)

    response = client.get(ENDPOINT)

    # assert
    assert response.status_code == 200
    assert response.json["entries"][0]["author"] == AUTHOR
    assert response.json["entries"][0]["text"] == TEXT


def test_guestbook_3(client):
    # arrange
    ENDPOINT = "/guest-book"
    AUTHOR_1 = "Jean"
    TEXT_1 = "Bonjour,"
    AUTHOR_2 = "Michel"
    TEXT_2 = "Yoo"
    
    # act
    with client.application.app_context():
        guest_book_POST(AUTHOR_1, TEXT_1)
        guest_book_POST(AUTHOR_2, TEXT_2)

    response = client.get(ENDPOINT)

    # assert
    assert response.status_code == 200
    assert response.json["entries"][0]["author"] == AUTHOR_2
    assert response.json["entries"][0]["text"] == TEXT_2
    assert response.json["entries"][1]["author"] == AUTHOR_1
    assert response.json["entries"][1]["text"] == TEXT_1

