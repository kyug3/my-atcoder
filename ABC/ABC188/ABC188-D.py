N, C = map(int, input().split())
lst = []
for _ in range(N):
    a, b, c = map(int, input().split())
    lst.append((a, c))
    lst.append((b + 1, -c))

lst.sort()
ans = 0
date = lst[0][0]
c_total = 0
for d, c in lst:
    ans += min(c_total, C) * (d - date)
    c_total += c
    date = d
    
print(ans)