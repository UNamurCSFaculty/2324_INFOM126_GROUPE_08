from api import create_app
from config import API


if __name__ == '__main__':
    app = create_app()
    app.run(host=API.HOST, port=API.PORT)
