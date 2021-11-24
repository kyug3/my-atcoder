import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))


def update(l, r, v):
    # 区間[l, r) に vを足す
    L = l + M
    R = r + M
    while L < R:
        if R % 2 == 1:
            data[R-1] += v
            #data[R-1] %= mod
            r -= 1
        if L % 2 == 1:
            data[L] += v
            #data[L] %= mod
            L += 1
        L //= 2; R //= 2

def query(x):
    # x の総和を求める
    idx = x + M
    ans = data[idx]# % mod
    while True:
        idx //= 2
        if idx == 0:
            break
        ans += data[idx]
        #ans %= mod
    return ans

N, M = li()
inp = [li() for _ in range(N)]
data = [0] * (2*M+1)

for l, r, s in inp:
    update(l-1, r, s)

x = INF
idx = -1
for i in range(M):
    y = query(i)
    if y < x:
        x = y
        idx = i

ans = 0
for l, r, s in inp:
    if l-1 <= idx <= r-1:
        continue
    ans += s
print(ans)