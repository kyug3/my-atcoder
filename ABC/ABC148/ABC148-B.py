import sys
input = sys.stdin.readline

N = int(input())
S, T = input().rstrip().split()
ans = ""
for s, t in zip(S, T):
    ans += s + t
print(ans)