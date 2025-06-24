from abc import ABC, abstractmethod

class Duck(ABC):
    @abstractmethod
    def swim(self):
        pass


class RealDuck(Duck):
    def swim(self):
        pass


class RubberDuck(Duck):
    def swim(self):
        pass

    def insertBatteries(self):
        pass


