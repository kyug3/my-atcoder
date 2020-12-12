import sys
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

ans = 0
for s, t in zip(S, T):
    if s == t:
        ans += 1
print(ans)