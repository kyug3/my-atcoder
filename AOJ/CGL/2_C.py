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

class Segment:
    def __init__(self, v1, v2):
        self.p1 = v1
        self.p2 = v2

def cross_point(p1, p2, p3, p4) -> Vector:
    s1 = Segment(p1, p2)
    s2 = Segment(p3, p4)
    base = s2.p2 - s2.p1
    d1 = abs(base.cross(s1.p1 - s2.p1))
    d2 = abs(base.cross(s1.p2 - s2.p1))
    t = d1 / (d1 + d2)
    return s1.p1 + (s1.p2 - s1.p1) * t

for _ in range(int(input())):
    x1, y1, x2, y2, x3, y3, x4, y4= map(int, input().split())
    p1, p2, p3, p4 = Vector(x1, y1), Vector(x2, y2), Vector(x3, y3), Vector(x4, y4)
    ans = cross_point(p1, p2, p3, p4)
    print(ans.x, ans.y)
