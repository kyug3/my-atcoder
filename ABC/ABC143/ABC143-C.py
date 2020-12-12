import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()

ans = 0
last = ""
for s in S:
    if last != s:
        ans += 1
        last = s
print(ans)