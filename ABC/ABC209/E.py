import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))
from collections import defaultdict, deque

N = int(input())
head = defaultdict(list)
tail = defaultdict(list)
S = [(input(), i) for i in range(N)]
for s, i in S:
    head[s[:3]].append(i)
    tail[s[-3:]].append(i)

edge = [[] for _ in range(N)]
ans = [0] * N
deg = [0] * N
deq = deque()
for s, i in S:
    x = s[:3]
    y = s[-3:]
    if not y in head:
        ans[i] = -1
        deq.append(i)
    for v in tail[x]:
        edge[i].append(v)
        deg[v] += 1

while deq:
    x = deq.popleft()
    for y in edge[x]:
        if ans[y]: continue
        if ans[x] == 1:
            deg[y] -= 1
            if deg[y] == 0:
                deq.append(y)
                ans[y] = -1
        elif ans[x] == -1:
            deq.append(y)
            ans[y] = 1

for a in ans:
    if a == -1:
        print('Takahashi')
    elif a == 1:
        print('Aoki')
    else:
        print('Draw')