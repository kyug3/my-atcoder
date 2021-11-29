import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N, a = li()
k = int(input())
B = li()

a -= 1
B = [b-1 for b in B]

dist = [-1] * N
now = a
for i in range(N**2):
    if dist[now] >= 0:
        heiro_start = now
        break
    dist[now] = i
    now = B[now]

len_heiro = max(dist) - dist[heiro_start] + 1
if k - dist[heiro_start] < 0:
    idx = dist.index(k)
    print(idx+1)
    exit()
k -= dist[heiro_start]

heiro = []
seen = [0] * N 
now = heiro_start
while not seen[now]:
    seen[now] = 1
    heiro.append(now)
    now = B[now]
print(heiro[k%len_heiro] + 1)