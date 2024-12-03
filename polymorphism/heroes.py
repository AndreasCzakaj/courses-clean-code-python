from abc import ABC, abstractmethod

class Hero(ABC):
    @abstractmethod
    def useForce():
        pass


class Storm(Hero):
    def useForce():
        return "pust, pust"


class Leader:
    def __init__(self):
        self.heroes = {}

    def selectHero(self, heroName: str) -> Hero:
        pass