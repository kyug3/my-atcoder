N = int(input())
S = [list(input()) for _ in range(N)]

ans = ''
for i in range(ord('a'), ord('z') + 1):
    x = chr(i)
    min_x = 100
    for s in S:
        if not x in s:
            break
        min_x = min(min_x, s.count(x))
    else:
        ans += x * min_x
print(ans)