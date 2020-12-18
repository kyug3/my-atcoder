import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))

now = 1
ans = 0
for x in a:
    if x == now:
        now += 1
    else:
        ans += 1
if now == 1:
    print(-1)
else:
    print(ans)