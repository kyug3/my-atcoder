import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def norm(self):
        return self.x ** 2 + self.y ** 2

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(other * self.x, other * self.y)

    def __truediv__(self, other):
        return Vector(other / self.x, other / self.y)

    def dot(self, other):
        # 内積
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        # 外積
        return self.x * other.y - self.y * other.x
    
    def is_orthogonal(self, other):
        # 直交判定
        return self.dot(other) == 0.0
    
    def is_parallel(self, other):
        return self.cross(other) == 0.0

    def scale(self, n):
        # スカラー倍
        return Vector(self.x * n, self.y * n)

    def length(self):
        # ベクトルの長さ
        return math.sqrt(self.x ** 2 + self.y ** 2)

class Segment:
    def __init__(self, v1, v2):
        self.p1 = v1
        self.p2 = v2

class Polygon:
    def __init__(self, points):
        self.points = points
    
    def area(self):
        a = 0
        for i in range(-1, len(self.points) - 1):
            a += ((self.points[i].x - self.points[i+1].x)
                  * (self.points[i].y + self.points[i+1].y))
        return abs(a) / 2

vs = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    vs.append(Vector(x, y))

ply = Polygon(vs)
print(ply.area())