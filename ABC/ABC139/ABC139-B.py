import sys
input = sys.stdin.readline

A, B = map(int, input().split())
ans = 0
tap = 1
while True:
    if tap >= B:
        break
    ans += 1
    tap += A - 1
print(ans)