import sys
input = sys.stdin.readline

a, b =  input().rstrip().split()
ab = int(a + b)

ans = "No"
for n in range(1, ab):
    if ab == n ** 2:
        ans = "Yes"
print(ans)