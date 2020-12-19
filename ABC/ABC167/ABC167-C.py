import numpy as np

N, M, X = map(int, input().split())
CA = [list(map(int, input().split())) for _ in range(N)]
ans = float('inf')
for i in range(2 ** N):
    array = np.zeros(M)
    cost = 0
    for j in range(N):
        if (i >> j) & 1:
            array += np.array(CA[j][1:])
            cost += CA[j][0]
    if np.amin(array) >= X:
        ans = min(ans, cost)
    
if ans == float('inf'):
    print(-1)
else:
    print(ans)