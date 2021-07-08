import sys, math
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

S = input()
ans = 100000000
for i in range(len(S)-2):
    ans = min(ans, abs(753 - int(S[i] + S[i+1] + S[i+2])))
print(ans)