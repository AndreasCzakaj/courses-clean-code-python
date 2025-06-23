
from dataclasses import dataclass

# Data classes for Position and Vector
@dataclass
class Position:
    x: int
    y: int
    z: int

    @classmethod
    def builder(cls):
        return PositionBuilder()



class PositionBuilder:
    def __init__(self):
        self._x = 0
        self._y = 0
        self._z = 0

    def x(self, x: int):
        self._x = x
        return self

    def y(self, y: int):
        self._y = y
        return self

    def z(self, z: int):
        self._z = z
        return self

    def build(self) -> Position:
        return Position(self._x, self._y, self._z)





@dataclass
class Vector:
    x: int
    y: int
    z: int

    @classmethod
    def builder(cls):
        return VectorBuilder()


class VectorBuilder:
    def __init__(self):
        self._x = 0
        self._y = 0
        self._z = 0

    def x(self, x: int):
        self._x = x
        return self

    def y(self, y: int):
        self._y = y
        return self

    def z(self, z: int):
        self._z = z
        return self

    def build(self) -> Vector:
        return Vector(self._x, self._y, self._z)