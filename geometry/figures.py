from abc import ABC, abstractmethod
from math import pi, sqrt, isclose
from typing import List

class Figure(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Circle(Figure):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return pi * self.radius ** 2

class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float) -> None:
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_angled(self) -> bool:
        sides = sorted([self.a, self.b, self.c])
        return isclose(sides[2] ** 2, sides[0] ** 2 + sides[1] ** 2) 