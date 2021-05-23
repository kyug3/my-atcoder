import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))
from collections import deque
def bfs(start, num_node):
    queue = deque([start])
    seen = [0] * (num_node)
    seen[start] = 1
    while queue:
        x = queue.popleft()
        for y in graph[x]:
            if seen[y]:
                continue
            seen[y] = seen[x] + 1
            queue.append(y)
    return seen

N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = li()
    a -= 1; b -= 1
    graph[a].append(b)
    graph[b].append(a)

seen = bfs(0, N)

ans1 = []
ans2 = []
for i in range(N):
    if seen[i] % 2:
        ans1.append(i+1)
    else:
        ans2.append(i+1)
if len(ans2) > len(ans1):
    ans1 = ans2

print(*ans1[:N//2])