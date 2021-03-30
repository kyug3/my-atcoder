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

def counter_clockwise(p0, p1, p2):
    # 3点 p0, p1, p2について
    # v1 = p1 - p0
    # v2 = p2 - p0
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

def intersect(p1, p2, p3, p4):
    # 線分p1p2と線分p3p4の交差判定
    return (counter_clockwise(p1, p2, p3) * counter_clockwise(p1, p2, p4) <= 0
            and counter_clockwise(p3, p4, p1) * counter_clockwise(p3, p4, p2) <= 0)

for _ in range(int(input())):
    x0, y0, x1, y1, x2, y2, x3, y3 = map(int, input().split())
    p1, p2, p3, p4 = Vector(x0, y0), Vector(x1, y1), Vector(x2, y2), Vector(x3, y3)
    print(1 if intersect(p1, p2, p3, p4) else 0)