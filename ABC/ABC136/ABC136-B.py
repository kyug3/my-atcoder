import sys
input = sys.stdin.readline

N = int(input())
ans = 0
for n in range(1, N + 1):
    if len(str(n)) % 2 == 1:
        ans += 1
print(ans)