# Classifies a triangle given three points as equilateral, isosceles, scalene, right-angled, or invalid using side lengths and geometry rules.
import math


def calculate_side_length(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def is_valid_triangle(a, b, c):
    # Check triangle inequality and positive sides
    return (a + b > c) and (b + c > a) and (c + a > b) and (a > 0 and b > 0 and c > 0)


def is_equilateral(a, b, c, tol):
    # All sides equal within tolerance
    return abs(a - b) < tol and abs(b - c) < tol


def is_scalene(a, b, c, tol):
    # All sides different beyond tolerance
    return abs(a - b) > tol and abs(b - c) > tol and abs(a - c) > tol


def is_isosceles(a, b, c, tol):
    # At least two sides equal but not equilateral
    return (
        abs(a - b) < tol or abs(b - c) < tol or abs(a - c) < tol
    ) and not is_equilateral(a, b, c, tol)


def is_right_triangle(a, b, c, tol):
    sides = sorted([a, b, c])
    return abs(sides[2] ** 2 - (sides[0] ** 2 + sides[1] ** 2)) < tol


def classify_triangle(p1, p2, p3, tol=1e-9):
    a = calculate_side_length(p1, p2)
    b = calculate_side_length(p2, p3)
    c = calculate_side_length(p3, p1)
    if not is_valid_triangle(a, b, c):
        return "Invalid Triangle."
    elif is_equilateral(a, b, c, tol):
        return "Equilateral Triangle."
    elif is_right_triangle(a, b, c, tol) and is_isosceles(a, b, c, tol):
        return "Isosceles Right Triangle."
    elif is_right_triangle(a, b, c, tol):
        return "Right Triangle."
    elif is_isosceles(a, b, c, tol):
        return "Isosceles Triangle."
    elif is_scalene(a, b, c, tol):
        return "Scalene Triangle."
    else:
        return "Error!"

check=classify_triangle((1, 2), (4, 5), (1, 2))
print(check)