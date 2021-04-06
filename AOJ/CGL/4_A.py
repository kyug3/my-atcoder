import math
EPS =  1e-10

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
    
    def __repr__(self):
        return repr((self.x, self.y))

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

    def size(self):
        return len(self.points)
    
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
    
    def contains(self, point):
        # 点が多角形に内包されるか判定
        # 2 内包, 1 辺上, 0 それ以外
        n = len(self.points)
        x = False
        for i in range(n):
            a = self.points[i] - p
            b = self.points[(i+1) % n] - p
            if abs(a.cross(b)) < EPS  and a.dot(b) < EPS:
                return 1
            if a.y > b.y:
                a, b = b, a
            if a.y < EPS and EPS < b.y and a.cross(b) > EPS:
                x = False if x else True
        return 2 if x else 0

    def andrew_scan(self):
        if self.size() < 3:
            return self.points

        u, l = [], []
        #s = sorted(self.points, key=lambda x: (x.x, x.y)) 
        s = sorted(self.points, key=lambda x: (x.y, x.x))
        u.append(s[0])
        u.append(s[1])
        l.append(s[-1])
        l.append(s[-2])

        for i in range(2, len(s)):
            n = len(u)
            #while n >= 2 and ccw(u[n-2], u[n-1], s[i]) != -1: 辺上の点を含めない場合
            while n >= 2 and ccw(u[n-2], u[n-1], s[i]) == 1: 
                u.pop()
                n -= 1
            u.append(s[i])

        for i in range(len(s) - 3, -1, -1):
            n = len(l)
            #while n >= 2 and ccw(l[n-2], l[n-1], s[i]) != -1: 辺上の点を含めない場合
            while n >= 2 and ccw(l[n-2], l[n-1], s[i]) == 1:
                l.pop()
                n -= 1
            l.append(s[i])

        # 反時計回りに並べる
        l = l[::-1]
        for i in range(len(u) - 2, 0, -1):
            l.append(u[i])

        return l


def projection(segment: Segment, point: Vector):
    # 線分p1p2に点pから垂線を引いた交点xを求める
    base = segment.p2 - segment.p1
    hypo = point - segment.p1
    r = hypo.dot(base) / base.norm()
    x = base.scale(r) + segment.p1
    return x

def reflect(segment: Segment, point:Vector):
    # 線分p1p2を対称軸として点pと線対称の位置にある点xを求める
    return point + (projection(segment, point) - point) * 2

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

def intersect(p1, p2, p3, p4):
    # 線分p1p2と線分p3p4の交差判定
    return (ccw(p1, p2, p3) * ccw(p1, p2, p4) <= 0
            and ccw(p3, p4, p1) * ccw(p3, p4, p2) <= 0)

def cross_point(p1, p2, p3, p4) -> Vector:
    # 線分p1p2と線分p3p4の交点
    s1 = Segment(p1, p2)
    s2 = Segment(p3, p4)
    base = s2.p2 - s2.p1
    d1 = abs(base.cross(s1.p1 - s2.p1))
    d2 = abs(base.cross(s1.p2 - s2.p1))
    t = d1 / (d1 + d2)
    return s1.p1 + (s1.p2 - s1.p1) * t

def dist_LP(line: Segment, point):
    # 点p と 直線p1p2 の距離
    p = line.p2 -line.p1
    return (abs((line.p2 - line.p1).cross(point - line.p1))
           / p.length())

def dist_SP(s, p):
    # 線分sと点p の距離
    if (s.p2 - s.p1).dot(p - s.p1) < 0:
        p -= s.p1
        return p.length()
    if (s.p1 - s.p2).dot(p - s.p2) < 0:
        p -= s.p2
        return p.length()
    return dist_LP(s, p)

def dist_SS(s1, s2):
    # 線分と線分の距離
    if intersect(s1.p1, s1.p2, s2.p1, s2.p2): return 0
    return min((dist_SP(s1, s2.p1),
                dist_SP(s1, s2.p2),
                dist_SP(s2, s1.p1),
                dist_SP(s2, s1.p2)))

lst = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    lst.append(Vector(x, y))

ply = Polygon(lst)
A = ply.andrew_scan()
print(len(A))
for a in A:
    print(a.x, a.y)