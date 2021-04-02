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
    
    def is_convex(self):
        n = len(self.points)
        for i in range(n):
            x = ccw(self.points[(i+1)%n], self.points[i%n], self.points[(i+2)%n])
            if x == 1:
                return False
        return True

def ccw(p0, p1, p2):
    # counter clockwise
    # 3点 p0, p1, p2について
    v1 = p1 - p0
    v2 = p2 - p0
    if v1.cross(v2) > 0:
        # p1からp2が反時計回り
        return 1
    elif v1.cross(v2) < 0:
        # 時計回り
        return -1
    elif v1.dot(v2) < 0:
        # p2, p0, p1の順で同一直線上
        return 2
    elif v2.norm() > v1.norm():
        # p0, p1, p2の順で同一直線上
        return -2
    else:
        # p2が線分p0p1上
        return 0

vs = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    vs.append(Vector(x, y))

ply = Polygon(vs)
print(1 if ply.is_convex() else 0)