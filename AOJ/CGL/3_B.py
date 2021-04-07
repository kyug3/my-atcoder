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

def is_convex(A):
    n = len(A)
    for i in range(n):
        x = ccw(A[(i+1)%n], A[i%n], A[(i+2)%n])
        if x == 1:
            return False
    return True

vs = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    vs.append((x, y))

print(1 if is_convex(vs) else 0)