import sys, math
sys.setrecursionlimit(1000000)
INF = 1 << 100
mod = 1000000007
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))


N, K = li()
if K >= N:
    print(0)
    exit()
H = li()
dic = {e: i for e, i in enumerate(set(H))}
dic2 = {v: k for k, v in dic.items()}
now = [[INF] * (K+2) for _ in range(len(dic))]
for i in range(len(dic)):
    if dic[i] == H[0]:
        now[i][0] = dic[i]
    else:
        now[i][1] = dic[i]

for i in range(1, N): # i列目
    nxt = [[INF] * (K+2) for _ in range(len(dic))]
    for j in range(len(dic)): # 高さ
        for k in range(K+1)[::-1]: # 操作回数
            if now[j][k] == INF:
                continue
            if dic[j] == H[i]:
                nxt[j][k] = min(nxt[j][k], now[j][k])
            else:
                # Hiをjに変える
                nxt[j][k+1] = min(nxt[j][k+1], now[j][k])
                # 変えない
                if H[i] > dic[j]:
                    nxt[dic2[H[i]]][k] = min(nxt[dic2[H[i]]][k], now[j][k] + H[i] - dic[j])
                else:
                    nxt[dic2[H[i]]][k] = min(nxt[dic2[H[i]]][k], now[j][k])
    now = nxt

ans = INF
for i in range(len(dic)):
    ans = min(ans, min(now[i][:K+1]))
print(ans)


