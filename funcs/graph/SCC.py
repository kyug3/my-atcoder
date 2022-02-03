"""
入力
G: 有向グラフ
G2: 逆向きの有向グラフ

N, M = li()
G = [[] for _ in range(N)]
G2 = [[] for _ in range(N)]
for _ in range(M):
    a, b = li()
    a -= 1; b -= 1
    G[a].append(b)
    G2[b].append(a)
"""
def scc(N, G, G2):
    """
    G: 有向グラフ
    G2: 逆向きの有向グラフ
    """
    order = []
    seen = [0] * N
    label = [0] * N
    num_group = [0] * N
    
    def dfs(n):
        seen[n] = 1
        stack = [n, n]
        while stack:
            n = stack.pop()
            if seen[n]:
                order.append(n)
            for x in G[n]:
                if seen[x]:
                    continue
                stack.append(x)
                stack.append(x)
                seen[x] = 1
    
    for i in range(N):
        if seen[i]: continue
        dfs(i)
    
    seen = [0] * N
    def reversed_dfs(n, l):
        seen[n] = 1
        num_group[l] += 1
        label[n] = l

        stack = [n]
        while stack:
            n = stack.pop()
            for x in G2[n]:
                if seen[x]:
                    continue
                seen[x] = 1
                num_group[l] += 1
                label[x] = l
                stack.append(x)

    now = -1
    for i in order[::-1]:
        if seen[i]:
            continue
        now += 1
        reversed_dfs(i, now)
    return label, num_group
