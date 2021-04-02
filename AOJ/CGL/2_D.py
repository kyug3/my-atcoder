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

def intersect(p1, p2, p3, p4):
    # 線分p1p2と線分p3p4の交差判定
    return (ccw(p1, p2, p3) * ccw(p1, p2, p4) <= 0
            and ccw(p3, p4, p1) * ccw(p3, p4, p2) <= 0)

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
    

def dist_LP(line: Segment, point):
    p = line.p2 -line.p1
    return (abs((line.p2 - line.p1).cross(point - line.p1))
           / p.length())

def dist_SP(s, p):
    if (s.p2 - s.p1).dot(p - s.p1) < 0:
        p -= s.p1
        return p.length()
    if (s.p1 - s.p2).dot(p - s.p2) < 0:
        p -= s.p2
        return p.length()
    return dist_LP(s, p)

def dist_SS(s1, s2):
    if intersect(s1.p1, s1.p2, s2.p1, s2.p2): return 0
    return min((dist_SP(s1, s2.p1),
                dist_SP(s1, s2.p2),
                dist_SP(s2, s1.p1),
                dist_SP(s2, s1.p2)))

for _ in range(int(input())):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    s1 = Segment(Vector(x1, y1), Vector(x2, y2))
    s2 = Segment(Vector(x3, y3), Vector(x4, y4))
    print(dist_SS(s1, s2))