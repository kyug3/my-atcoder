import sys
input = sys.stdin.readline

W, H, x, y = map(int, input().split())
ans = W * H / 2
if W == x * 2 and H == y * 2:
    print(ans, 1)
else:
    print(ans, 0)