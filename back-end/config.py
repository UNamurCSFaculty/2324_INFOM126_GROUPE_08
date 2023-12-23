import os


class Database:
    HOST = os.getenv('DB_HOST')
    PORT = os.getenv('DB_PORT')
    USERNAME = os.getenv('POSTGRES_USER')
    PASSWORD = os.getenv('POSTGRES_PASSWORD')
    DB = os.getenv('POSTGRES_DB')

    @classmethod
    def URI(cls):
        return "postgresql://{}:{}@{}:{}/{}".format(
            cls.USERNAME, cls.PASSWORD, cls.HOST, cls.PORT, cls.DB
        )


class API:
    HOST = "0.0.0.0"
    PORT = 5000
