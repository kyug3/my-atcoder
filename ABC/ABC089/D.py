import sys, math
from collections import deque, defaultdict
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))


H, W, D = li()
dic = defaultdict(list)
for i in range(H):
    A = li()
    for j in range(W):
        dic[A[j]] = [i+1, j+1]
Q = int(input())

def cost(p1, p2):
    return sum(abs(a - b) for a, b in zip(p1, p2))

memo = [[0] for _ in range(D)]

for i in range(1, D+1):
    memo[i%D].append(cost(dic[i], dic[i+D]))
    for j in range(i+D, H*W-D+1, D):
        memo[i%D].append(memo[i%D][-1] + cost(dic[j], dic[j+D]))

ans = 0
for _ in range(Q):
    L, R = li()
    if L % D:
        L += D
        R += D
    print(memo[L%D][R//D-1] - memo[L%D][L//D-1])
    