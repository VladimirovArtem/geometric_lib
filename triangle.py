def area(a, b, c):
    # Проверка на корректность треугольника
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Sides must be positive")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid triangle sides")

    s = (a + b + c) / 2  # Полупериметр
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5  # Формула Герона


def perimeter(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Sides must be positive")
    return a + b + c
