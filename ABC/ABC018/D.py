import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N, M, P, Q, R = li()
choco = [[] for _ in range(N)]
for _ in range(R):
    x, y ,z = li()
    x -= 1; y -= 1
    choco[x].append((y, z))

ans = 0
for i in range(2 ** N):
    cnt = 0
    men = [0] * M
    for j in range(N):
        if (i >> j) & 1:
            cnt += 1
            if cnt > P:
                break
            for k, z in choco[j]:
                men[k] += z
    if cnt > P:
        continue
    men.sort(reverse=True)
    ans = max(ans, sum(men[:Q]))

print(ans)

