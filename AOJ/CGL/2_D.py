import math
EPS = 1e-10

def dot(a: list, b: list) -> int:
    # 内積
    return sum(x * y for x, y in zip(a, b))

def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]

def norm(a: list) -> int:
    return a[0] ** 2 + a[1] ** 2

def length(a):
    return math.sqrt(sum(x ** 2 for x in a))

def add(a, b):
    return [x + y for x, y in zip(a, b)]

def subtract(a, b):
    return [x - y for x, y in zip(a, b)]

def scale(a, x):
    return [x * i for i in a]

def project(p1, p2, p3):
    # 線分p1p2に点p3から垂線を引いた交点xを求める
    base = subtract(p2, p1)
    hypo = subtract(p3, p1)
    r = dot(base, hypo) / norm(base)
    return add(scale(base, r), p1)

def reflect(p1, p2, p3):
    # 線分p1p2を対称軸として点p3と線対称の位置にある点xを求める
    return add(p3, scale(subtract(project(p1, p2, p3), p3), 2))

def ccw(p1, p2, p3):
    # counter clockwise
    # 3点 p1, p2, p3について
    v1 = subtract(p2, p1)
    v2 = subtract(p3, p1)
    if cross(v1, v2) > 0:
        # p2からp3が反時計回り
        return 1
    elif cross(v1, v2) < 0:
        # 時計回り
        return -1
    elif dot(v1, v2) < 0:
        # p3, p1, p2の順で同一直線上
        return 2
    elif norm(v2) > norm(v1):
        # p1, p2, p3の順で同一直線上
        return -2
    else:
        # p3が線分p1p2上
        return 0

def is_orthogonal(p1, p2, p3, p4):
    # p1p2を通る直線とp3p4を通る直線が直交するか判定
    v1 = subtract(p2, p1)
    v2 = subtract(p4, p3)
    return dot(v1, v2) == 0.0

def is_parallel(p1, p2, p3, p4):
    # p1p2を通る直線とp3p4を通る直線が平行か判定
    v1 = subtract(p2, p1)
    v2 = subtract(p4, p3)
    return cross(v1, v2) == 0.0

def intersect(p1, p2, p3, p4):
    # 線分p1p2と線分p3p4の交差判定
    return (ccw(p1, p2, p3) * ccw(p1, p2, p4) <= 0
            and ccw(p3, p4, p1) * ccw(p3, p4, p2) <= 0)

def cross_point(p1, p2, p3, p4):
    base = subtract(p4, p3)
    d1 = abs(cross(base, subtract(p1, p3)))
    d2 = abs(cross(base, subtract(p2, p3)))
    t = d1 / (d1 + d2)
    return add(p1, scale(subtract(p2, p1), t))
    

def dist_LP(p1, p2, p3):
    # p1p2を通る直線 と 点p3の距離
    p = subtract(p2, p1)
    return abs(cross(subtract(p2, p1), subtract(p3, p1))) / length(p)


def dist_SP(p1, p2, p3):
    # 線分p1p2と点p3の距離
    if dot(subtract(p2, p1), subtract(p3, p1)) < 0:
        p3 = subtract(p3, p1)
        return length(p3)
    if dot(subtract(p1, p2), subtract(p3, p2)) < 0:
        p3 = subtract(p3, p2)
        return length(p3)
    return dist_LP(p1, p2, p3)


def dist_SS(p1, p2, p3, p4):
    # 線分p1p2と線分p3p4の距離
    if intersect(p1, p2, p3, p4): return 0
    return min((dist_SP(p1, p2, p3),
                dist_SP(p1, p2, p4),
                dist_SP(p3, p4, p1),
                dist_SP(p3, p4, p2)))

for _ in range(int(input())):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    p1, p2 = (x1, y1), (x2, y2)
    p3, p4 = (x3, y3), (x4, y4)
    print(dist_SS(p1, p2, p3, p4))