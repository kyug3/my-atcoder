N, M = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    g[a].append(b)
    g[b].append(a)

for x in g:
    print(len(x))