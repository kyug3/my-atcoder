N = int(input())
a = list(map(int, input().split()))
a.sort()

ans = float('inf')
for i in range(a[0], a[-1] + 1):
    count = 0
    for j in a:
        count += (j - i) ** 2
    ans = min(ans, count)
print(ans)