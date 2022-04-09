import sys, math
sys.setrecursionlimit(1000000)
INF = 1 << 100
#mod = 1000000007
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))

N = li()
G = [[] for _ in range(N)]
dic = {}
idx = [0] * N
for _ in range(N-1):
    a, b = li()
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)
    dic[(a, b)] = idx[a]
    dic[(b, a)] = idx[b]
    idx[a] += 1; idx[b] += 1

from collections import deque

def toposort(G, v, N):
    q = deque([v])
    topo = []
    par = [-1] * N
    while q:
        x = q.popleft()
        topo.append(x)
        for y in G[x]:
            if par[x] == y:
                continue
            par[y] = x
            q.append(y)
    return topo, par
topo, par = toposort(G, 0, N)
dp = []
dp2 = [0] * N
for i in range(N):
    dp.append([0] * (idx[i]))

# 頂点0についての木dp
# dp[i][j] -> 頂点iから、j番目の辺を使った時の(求めたい何か)
for x in reversed(topo):
    y = par[x]
    if y != -1:
        i = dic[(y, x)]
        dp[y][i] = 0
        dp2[y] = 0

for x in topo:
    l = len(dp[x])
    # 左からの累積何か
    leftmax = [0] * (l+2)
    for i in range(1, l+1):
        leftmax[i] = leftmax[i-1] * dp[x][i-1]

    # 右からの累積何か
    rightmax = [0] * (l+2)
    for i in range(1, l+1)[::-1]:
        rightmax[i] = rightmax[i+1] * dp[x][i-1]
    
    for i in range(l):
        y = G[x][i]
        if par[x] == y:
            continue
        j = dic[(y, x)]
        #左右の累積を使って求めたい何かを取る
        tmp = leftmax[i] * rightmax[i+2] + 1

        #頂点yからその親への辺のdpを更新
        dp[y][j] = 0
        dp2[y] = 0


for i in range(N):
    print(dp2[i])
