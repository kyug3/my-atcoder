import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

def pascals_triangle(n):
    # c[i][j] == iCj
    c = []
    for i in range(n):
        r = [0] * n
        r[0] = 1
        for j in range(1, i+1):
            r[j] = c[-1][j-1] + c[-1][j]
        c.append(r)
    return c

C = pascals_triangle(1005)

N, D = li()
X, Y = li()
if X % D or Y % D:
    print(0)
    exit()
X //= D; Y //= D
tot = 0
for i in range(N+1):
    j = N - i
    a = b = 0
    if i >= X and (i - X) % 2 == 0:
        a = C[i][(i-X) // 2]
    if j >= Y and (j - Y) % 2 == 0:
        b = C[j][(j-Y) // 2]
    tot += (a * b * C[N][i])

print(tot / 4**N)
