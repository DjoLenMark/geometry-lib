geometry
Библиотека для расчёта площадей геометрических фигур на Python.

Возможности
Круг (Circle): площадь по радиусу
Треугольник (Triangle): площадь по трём сторонам, проверка на прямоугольность
Лёгкое расширение: добавьте новую фигуру, просто создав класс-наследник Figure
Установка
Скопируйте папку geometry в ваш проект или установите через pip после публикации.

Пример использования
from geometry.figures import Circle, Triangle, Figure
from typing import List

# Создание фигур
circle = Circle(2)
triangle = Triangle(3, 4, 5)

# Универсальный список фигур
figures: List[Figure] = [circle, triangle]

for fig in figures:
    print(f"Площадь: {fig.area()}")

# Проверка треугольника на прямоугольность
if isinstance(triangle, Triangle):
    print("Прямоугольный?", triangle.is_right_angled())
Документация
Абстрактный класс Figure
class Figure(ABC):
    @abstractmethod
    def area(self) -> float:
        pass
Класс Circle
class Circle(Figure):
    def __init__(self, radius: float) -> None:
        ...
    def area(self) -> float:
        ...
Класс Triangle
class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float) -> None:
        ...
    def area(self) -> float:
        ...
    def is_right_angled(self) -> bool:
        ...
Тесты
Для запуска тестов:

pytest geometry/tests/
Лицензия
MIT
