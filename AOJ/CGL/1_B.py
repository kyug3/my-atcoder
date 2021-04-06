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

def project(p1, p2, p3):
    # 線分p1p2に点p3から垂線を引いた交点xを求める
    base = subtract(p2, p1)
    hypo = subtract(p3, p1)
    r = dot(base, hypo) / norm(base)
    return add(scale(base, r), p1)

def reflect(p1, p2, p3):
    return add(p3, scale(subtract(project(p1, p2, p3), p3), 2))

x1, y1, x2, y2 = map(int, input().split())
p1 = [x1, y1]
p2 = [x2, y2]
for _ in range(int(input())):
    p3 = list(map(int, input().split()))
    print(*reflect(p1, p2, p3))
