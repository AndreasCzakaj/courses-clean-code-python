from abc import ABC, abstractmethod

class Duck(ABC):
    @abstractmethod
    def swim():
        pass


class RealDuck(Duck):
    def swim():
        pass


class RubberDuck(Duck):
    def swim():
        pass

    def insertBatteries():
        pass


