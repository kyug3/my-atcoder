S = list(input())
last = S[-1]
ans = 0
while S:
    now = S.pop()
    if now != last:
        ans += 1
    last = now
print(ans)