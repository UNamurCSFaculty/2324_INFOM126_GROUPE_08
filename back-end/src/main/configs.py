class Database:
    HOST = "database"
    PORT = 5432
    USERNAME = "postgres"
    PASSWORD = "grespost"
    DB = "INFOM126"

    @classmethod
    def URI(cls):
        return "postgresql://{}:{}@{}:{}/{}".format(
            cls.USERNAME, cls.PASSWORD, cls.HOST, cls.PORT, cls.DB
        )


class API:
    HOST = "0.0.0.0"
    PORT = 5000
