import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N, D = li()

P = []
C = []
for i in range(1, N+1):
    p, c = li()
    P.append(p)
    C.append(c)

def dfs(idx, seen, score, cnt):
    rest = D - score
    points = (idx + 1) * 100
    if points * P[idx] >= rest:
        return cnt + ((rest + points - 1) // (points))

    score += points * P[idx] + C[idx]
    cnt += P[idx]
    if score >= D:
        return cnt
    seen |= (1 << idx)
    ret = INF
    for i in range(N):
        if (seen >> i) & 1:
            continue
        ret = min(dfs(i, seen, score, cnt), ret)
    return ret

ans = INF
for i in range(N):
    ans = min(ans, dfs(i, 0, 0, 0))

print(ans)