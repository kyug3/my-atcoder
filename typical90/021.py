import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N, M = li()
G = [[] for _ in range(N)]
G2 = [[] for _ in range(N)]
for _ in range(M):
    a, b = li()
    a -= 1; b -= 1
    G[a].append(b)
    G2[b].append(a)

def scc(N, G, G2):
    order = []
    seen = [0] * N
    label = [0] * N     # 各頂点のラベルが同じなら連結
    num_group = [0] * N # ラベルごとの頂点数
    
    def dfs(n):
        seen[n] = 1
        for x in G[n]:
            if seen[x]:
                continue
            dfs(x)
        order.append(n)
    
    for i in range(N):
        if seen[i]: continue
        dfs(i)
    
    seen = [0] * N
    def reversed_dfs(n, l):
        seen[n] = 1
        num_group[l] += 1
        label[n] = l
        for x in G2[n]:
            if seen[x]:
                continue
            reversed_dfs(x, l)

    now = -1
    for i in reversed(order):
        if seen[i]:
            continue
        now += 1
        reversed_dfs(i, now)
        
    ans = 0
    for i in num_group:
        if i == 0:
            break
        i -= 1
        ans += (i+1) * i // 2
    print(ans)

scc(N, G, G2)