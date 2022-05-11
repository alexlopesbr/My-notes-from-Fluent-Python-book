# 1.2 | 35 | a simple two-dimensional vector class


from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.x + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


soma = Vector(2, 4) + Vector(2, 4)

print(soma)
print(abs(soma))
print(bool(soma))
print(abs(soma) * 3)
