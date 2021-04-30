import sys, math
from collections import deque, defaultdict
from itertools import permutations
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N, M, R = li()
r = li()
r = [x-1 for x in r]

am = [[0 if i == j else float('inf') for j in range(N)]
      for i in range(N)]
for _ in range(M):
    a, b, c = li()
    a -= 1; b -= 1
    am[a][b] = c
    am[b][a] = c

def floyd_warshall(num_node):
    # am = adjacency matrix
    for k in range(num_node):
        for i in range(num_node):
            for j in range(num_node):
                am[i][j] = min(am[i][j], am[i][k] + am[k][j])

floyd_warshall(N)
ans = float('inf')
for p in permutations(r):
    x = 0
    for i in range(1, R):
        x += am[p[i-1]][p[i]]
    ans = min(ans, x)
print(ans)