class MyService:
    def doStuff(self, input: int, type: str):
        if input == 1:
            raise ValueError("1")
        if input == 2:
            raise MyCustomError("2")
        if input == 3:
            raise MyIoError("3")

        
class MyClient:
    def consumeStuff(self, input: int):
        service = MyService()
        try:
            service.doStuff(input)
        except ServiceError:
            return 1
        except MyCustomError:
            return 2

from abc import ABC, abstractmethod

class ServiceError(ABC, Exception):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"{self.message})"
    

class MyCustomError(ServiceError):
    def __init__(self, message):
        super().__init__(message)
    
class MyIoError(ServiceError):
    def __init__(self, message):
        super().__init__(message)