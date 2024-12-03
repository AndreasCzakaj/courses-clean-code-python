class Main:
    def start():
        app = App()
        app.begin()

class App:
    def begin():
        service = SomeService()
        service.process()     

class SomeService:
    def process():
        db = TheRealDatabase()
        db.load()     

class TheRealDatabase:
    def load():
        pass       




