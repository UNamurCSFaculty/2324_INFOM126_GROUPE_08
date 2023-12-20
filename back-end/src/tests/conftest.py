import pytest

from main.app import create_app
from config import Database


@pytest.fixture()
def app():
    app = create_app(Database.URI(), True)

    # extra setups

    # yield
    yield app

    # clean up / teardown


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
