def dot(a: list, b: list) -> int:
    # 内積
    return sum(x * y for x, y in zip(a, b))

def norm(a: list) -> int:
    return a[0] ** 2 + a[1] ** 2

def add(a, b):
    return [x + y for x, y in zip(a, b)]

def subtract(a, b):
    return [x - y for x, y in zip(a, b)]

def scale(a, x):
    return [x * i for i in a]

def projection(p1, p2, p3):
    # 線分p1p2に点pから垂線を引いた交点xを求める
    base = subtract(p2, p1)
    hypo = subtract(p3, p1)
    r = dot(base, hypo) / norm(base)
    return add(scale(base, r), p1)
