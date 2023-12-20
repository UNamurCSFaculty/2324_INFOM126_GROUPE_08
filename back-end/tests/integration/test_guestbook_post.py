from datetime import datetime
from api.models import Message
from api.database import db
from api.controllers import guest_book_POST


def test_guestbook_1(client):
    # arrange
    ENDPOINT = "/guest-book"
    AUTHOR = "Sieg"
    TEXT = "Hello"
    DATA = {"author": AUTHOR, "text": TEXT}
    SUCCESS_MESSAGE = "New message successfully saved !" 
    
    # act
    response = client.post(ENDPOINT, json=DATA)

    # assert
    assert response.status_code == 200
    assert response.json["message"] == SUCCESS_MESSAGE
    assert response.json["entry"]["author"] == AUTHOR
    assert response.json["entry"]["text"] == TEXT


def test_guestbook_2(client):
    # arrange
    ENDPOINT = "/guest-book"
    ERROR_MESSAGE = "Invalid request. Both author and text are required."

    # act
    response = client.post(ENDPOINT, json={})

    # assert
    assert response.status_code == 400
    assert response.json["message"] == ERROR_MESSAGE

