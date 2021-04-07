def dot(a: list, b: list) -> int:
    # 内積
    return sum(x * y for x, y in zip(a, b))

def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]

def norm(a: list) -> int:
    return a[0] ** 2 + a[1] ** 2

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

for _ in range(int(input())):
    i = list(map(int, input().split()))
    p1 = [i[0], i[1]]
    p2 = [i[2], i[3]]
    p3 = [i[4], i[5]]
    p4 = [i[6], i[7]]
    print(1 if intersect(p1, p2, p3, p4) else 0)