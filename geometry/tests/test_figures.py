import pytest
from geometry.figures import Circle, Triangle
from math import pi, isclose

# Тесты для Circle
def test_circle_area():
    c = Circle(1)
    assert isclose(c.area(), pi)

    c2 = Circle(2.5)
    assert isclose(c2.area(), pi * 2.5 ** 2)

def test_circle_area_zero():
    c = Circle(0)
    assert isclose(c.area(), 0)

# Тесты для Triangle
def test_triangle_area():
    t = Triangle(3, 4, 5)
    # Площадь прямоугольного треугольника со сторонами 3, 4, 5 = 6
    assert isclose(t.area(), 6)

def test_triangle_area_equilateral():
    t = Triangle(2, 2, 2)
    s = 3
    expected = (3 ** 0.5) / 4 * 2 ** 2
    assert isclose(t.area(), expected, rel_tol=1e-9)

def test_triangle_is_right_angled_true():
    t = Triangle(3, 4, 5)
    assert t.is_right_angled() is True

def test_triangle_is_right_angled_false():
    t = Triangle(2, 2, 3)
    assert t.is_right_angled() is False 