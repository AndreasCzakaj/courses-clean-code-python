from abc import ABC, abstractmethod

class DatabasePort(ABC):
    @abstractmethod
    def get():
        pass


class SomeService:
    def __init__(self, dao: DatabasePort):
        self.dao = dao

    def process(self):
        self.dao.get()    


class App:
    def __init__(self, service: SomeService):
        self.service = service

    def begin():
        service = SomeService()
        service.process()     


class Main:
    def __init__(self, app: App):
        self.app = app

    def start(self):
        self.app.begin()



class DatabaseAdapter(ABC):
    def get():
        db = TheRealDatabase()
        db.load()     


class TheRealDatabase:
    def load():
        pass       



dao     = DatabaseAdapter()
service = SomeService(dao)
app     = App(service)
main    = Main(app)
