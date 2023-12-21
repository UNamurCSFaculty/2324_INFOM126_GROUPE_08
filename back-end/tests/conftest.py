import pytest

from api import create_app
from config import Database


@pytest.fixture()
def app():
    app = create_app("sqlite:///:memory:")

    # extra setups
    app.config.update({
        "TESTING": True
    })

    # yield
    yield app

    # clean up / teardown


@pytest.fixture()
def client(app):
    return app.test_client()
