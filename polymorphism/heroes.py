from abc import ABC, abstractmethod

class Hero(ABC):
    @abstractmethod
    def useForce(self):
        pass


class Storm(Hero):
    def useForce(self):
        return "pust, pust"


class Leader:
    def __init__(self):
        self.heroes = {}

    def selectHero(self, heroName: str) -> Hero:
        pass