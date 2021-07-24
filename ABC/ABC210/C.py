import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))
from collections import deque, defaultdict

N, K = li()
C = li()
q = deque()
dic = defaultdict(int)
now = 0
ans = 0
for i in range(N):
    if i >= K:
        x = q.popleft()
        dic[x] -= 1
        if dic[x] == 0:
            now -= 1

    q.append(C[i])
    dic[C[i]] += 1
    if dic[C[i]] == 1:
        now += 1
    ans = max(ans, now)
print(ans)