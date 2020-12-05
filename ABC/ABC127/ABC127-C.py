import sys
input = sys.stdin.readline

N, M = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(M)]
can_pass = [0 for _ in range(N+2)]

for l, r in LR:
    can_pass[l] += 1
    can_pass[r+1] -= 1

count = 0
ans = 0
for x in can_pass:
    count += x
    if count == M:
        ans += 1
    elif ans > 0:
        break
print(ans)
