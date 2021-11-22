import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

N, M, D = li()
A = li()

end = [i for i in range(N)]
start = [i for i in range(N)]
for i in range(M):
    a = A[M-1 - i] - 1
    end[a], end[a+1] = end[a+1], end[a]
    b = A[i] - 1
    start[b], start[b+1] = start[b+1], start[b]

print(end, start)

nxt = [0] * N
nxt2 = [0] * N
for i in range(N):
    nxt[end[i]] = start[i]
    nxt2[start[i]] = end[i]

print(nxt2)