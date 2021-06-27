import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N, M, C = li()
B = li()
As = [li() for _ in range(N)]

ans = 0
for i in range(N):
    count = C
    for j in range(M):
        count += As[i][j] * B[j]
    if count > 0:
        ans += 1
print(ans)
