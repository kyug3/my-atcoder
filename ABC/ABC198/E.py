import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())
C = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    graph[a].append(b)
    graph[b].append(a)

colors = [0] * (10**5 + 1)
ans = [1]
def dfs(node, parent):
    colors[C[node]] += 1
    for x in graph[node]:
        if x == parent:
            continue
        if colors[C[x]] == 0:
            ans.append(x+1)
        dfs(x, node)
    colors[C[node]] -= 1

dfs(0, -1)
ans.sort()
for x in ans:
    print(x)