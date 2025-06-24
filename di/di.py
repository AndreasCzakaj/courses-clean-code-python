class Main:
    def start(self):
        app = App()
        app.begin()

class App:
    def begin(self):
        service = SomeService()
        service.process()     

class SomeService:
    def process(self):
        db = TheRealDatabase()
        db.load()     

class TheRealDatabase:
    def load(self):
        pass       




