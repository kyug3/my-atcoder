import sys, math
#sys.setrecursionlimit(1000000)
INF = 1 << 100
#mod = 1000000007
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))


def get_divisors(x: int) -> list:
    divisors = []
    for i in range(1, x+1):
        if i * i > x:
            break
        if x % i == 0:
            divisors.append(i)
            if x // i != i:
                divisors.append(x // i)
    return divisors

t = int(input())
out = []
for _ in range(t):
    a, b, c, d = li()
    oritot = a * b

    diva = get_divisors(a)
    divb = get_divisors(b)
    ans = (-1, -1)

    # a*bの約数を軸にXの候補を探索
    for A in diva:
        for B in divb:
            AB = A * B
            # X = ABの倍数でa+1より大きい最小の数
            X = (a+1 + AB - 1) // AB * AB
            if a < X <= c:
                # tot = oritotとXの素因数の差分の積
                # Yがtotの倍数ならOK
                tot = oritot // math.gcd(oritot, X)
                num = (b+1 + tot - 1) // tot
                if num:
                    tot *= num
                # Y = totの倍数でb+1より大きい最小の数
                Y = tot
                if b < Y <= d:
                    ans = (X, Y)

    out.append(ans)

for o in out:
    print(*o)