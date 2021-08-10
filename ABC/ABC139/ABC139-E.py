import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))
from collections import deque

N = int(input())
A = [li() for _ in range(N)]
idx = [0] * N

nxt = [(e+1, i[0]) for e, i in enumerate(A)]

ans = 0
while nxt:
    used = set()
    dq = deque(nxt)
    nxt = []
    while dq:
        a, b = dq.popleft()
        if a in used and b in used:
            continue
        elif a in used or b in used:
            nxt.append((a, b))
        else:
            if A[a-1][idx[a-1]] == b and A[b-1][idx[b-1]] == a:
                idx[a-1] += 1
                idx[b-1] += 1
                if idx[a-1] < N - 1:
                    nxt.append((a, A[a-1][idx[a-1]]))
                used.add(a)
                if idx[b-1] < N - 1:
                    nxt.append((b, A[b-1][idx[b-1]]))
                used.add(b)
    ans += 1

for a in idx:
    if a != N-1:
        ans = -1
print(ans)
