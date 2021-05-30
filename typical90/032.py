import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

from itertools import permutations

N = int(input())
A = [li() for _ in range(N)]
M = int(input())
XY = [set() for _ in range(N)]
for _ in range(M):
    x, y = li()
    x -= 1; y -= 1
    XY[x].add(y)
    XY[y].add(x)

lst = [i for i in range(N)]
ans = 10**9
for x in permutations(lst, N):
    total = 0
    for j in range(N):
        if not j == N-1:
            if x[j+1] in XY[x[j]]:
                break
        total += A[x[j]][j]
    else:
        ans = min(ans, total)

if ans == 10**9:
    ans = -1

print(ans)
