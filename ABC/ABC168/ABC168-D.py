import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

seen = [False for _ in range(N + 1)]
queue = deque([1])
while queue:
    room = queue.popleft()
    for r in G[room]:
        if seen[r]:
            continue
        seen[r] = room
        queue.append(r)
if False in seen[2:]:
    print('No')
else:
    print('Yes')
    for x in seen[2:]:
        print(x)