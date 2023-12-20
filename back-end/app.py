from api import create_app
from config import Database, API


if __name__ == '__main__':
    app = create_app(Database.URI())
    app.run(host=API.HOST, port=API.PORT)
