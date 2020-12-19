N = int(input())
ans = 0
for n in range(1, N + 1):
    if n % 3 == 0 or n % 5 == 0:
        continue
    ans += n
print(ans)