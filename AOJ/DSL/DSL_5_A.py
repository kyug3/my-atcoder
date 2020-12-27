N, T = map(int, input().split())
customers = [0 for _ in range(T + 1)]

for _ in range(N):
    l, r = map(int, input().split())
    customers[l] += 1
    customers[r] -= 1

num = 0
ans = 0
for c in customers:
    num += c
    ans = max(ans, num)
    
print(ans)