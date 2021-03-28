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

    def scale(self, n):
        # スカラー倍
        return Vector(self.x * n, self.y * n)

x0, y0, x1, y1 = map(int, input().split())
v1 = Vector(x1 - x0, y1 - y0)
for i in range(int(input())):
    x2, y2 = map(int, input().split())
    v2 = Vector(x2 - x0, y2 - y0)
    if v1.cross(v2) > 0:
        print('COUNTER_CLOCKWISE')
    elif v1.cross(v2) < 0:
        print('CLOCKWISE')
    elif v1.dot(v2) < 0:
        print('ONLINE_BACK')
    elif v2.norm() > v1.norm():
        print('ONLINE_FRONT')
    else:
        print('ON_SEGMENT')