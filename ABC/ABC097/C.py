import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

se = set()
S = list(input().rstrip())
K = int(input())
N = len(S)

for i in range(N):
    tmp = S[i]
    se.add(S[i])
    for j in range(i+1, min(N, i+6)):
        tmp += S[j]
        se.add(tmp)

print(sorted(list(se))[K-1])