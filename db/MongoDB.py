from flask_pymongo import PyMongo 


class MongoDB:
    _instance = None

    def __init__(self, app=None):
        self.mongo = PyMongo()
        if app:
            self.init_app(app)

    def init_app(self, app):
        self.mongo.init_app(app)
        MongoDB._instance=self

    #dekoratory
    @property
    def client(self):
        return self.mongo.cx

    @property
    def db(self):
        return self.mongo.db

    def get_collection(self, name):
        return self.mongo.db[name]

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            raise Exception("MongoDB instance is not iniciated")
        return cls._instance
