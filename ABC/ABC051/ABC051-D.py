from collections import defaultdict

def floyd_warshall(num_node):
    # am = adjacency matrix
    for k in range(num_node):
        for i in range(num_node):
            for j in range(num_node):
                am[i][j] = min(am[i][j], am[i][k] + am[k][j])
    return am

N, M = map(int, input().split())
am = [[0 if i == j else float('inf') for j in range(N)]
      for i in range(N)]
edges = defaultdict(int)

for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1; b -= 1
    if a > b:
        a, b = b, a
    am[a][b] = c
    am[b][a] = c
    edges[(a, b)] = c

dists = floyd_warshall(N)
ans = 0
for key, value in edges.items():
    a, b = key
    flag = True
    for i in range(N):
        for j in range(i+1, N):
            if dists[i][a] + value + dists[b][j] == dists[i][j]:
                flag = False
                break
    if flag:
        ans += 1
print(ans)