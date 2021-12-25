import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
#mod = 10**9 + 7
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))


# https://atcoder.jp/contests/abc013/tasks/abc013_4

N, M, D = li()
A = li()


amida = [i for i in range(N)]
for i in range(M):
    a = A[i]
    amida[a-1], amida[a] = amida[a], amida[a-1]

# ends[i][j] = 最初j番目だったものが2^i回操作して何番目になったか
ends = [[0] * N for _ in range(D.bit_length() + 1)]
for i in range(N):
    ends[1][amida[i]] = i
ends[0] = [i for i in range(N)]

for i in range(1, D.bit_length()):
    s = ends[i-1]
    e = ends[i]
    for j in range(N):
        ends[i+1][j] = e[e[j]]

for i in range(N):
    now = i
    x = D
    for j in range(D.bit_length()+1):
        if (x >> j) & 1:
            now = ends[j+1][now]
    print(now + 1)