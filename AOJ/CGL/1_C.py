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

def ccw(v1, v2):
    # counter clockwise
    # 3点 p0, p1, p2について
    # v1 = p1 - p0
    # v2 = p2 - p0
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



x0, y0, x1, y1 = map(int, input().split())
v1 = Vector(x1 - x0, y1 - y0)
for i in range(int(input())):
    x2, y2 = map(int, input().split())
    v2 = Vector(x2 - x0, y2 - y0)
    ret = ccw(v1, v2)
    if ret == 1:
        print('COUNTER_CLOCKWISE')
    elif ret == -1:
        print('CLOCKWISE')
    elif ret == 2:
        print('ONLINE_BACK')
    elif ret == -2:
        print('ONLINE_FRONT')
    else:
        print('ON_SEGMENT')