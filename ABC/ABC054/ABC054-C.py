N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    graph[a].append(b)
    graph[b].append(a)

ans = 0
seen = [0] * N
def dfs(parent):
    seen[parent] = 1
    if sum(seen) == N:
        global ans
        ans += 1
    for n in graph[parent]:
        if seen[n]:
            continue
        dfs(n)
    seen[parent] = 0

dfs(0)
print(ans) 
    