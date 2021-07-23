import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

M, K = li()
if 2**M <= K:
    print(-1)
    exit()
if K == 0:
    lst = []
    for i in range(2**M):
        lst.append(i)
        lst.append(i)
    print(*lst)
    exit()
if M <= 1:
    print(-1)
    exit()

from collections import deque
deq = deque([K])
for i in range(2**M):
    if i == K:
        continue
    deq.append(i)
    deq.appendleft(i)
deq.append(K)
print(*deq)
