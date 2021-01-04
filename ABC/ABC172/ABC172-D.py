def func(x):
    n = N // x
    return int((x + x * n) / 2 * n)

N = int(input())
ans = 0
for i in range(1, N + 1):
    ans += func(i)

print(ans)