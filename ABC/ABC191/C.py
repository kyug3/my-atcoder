H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

ans = 0
for h in range(H-1):
    for w in range(W-1):
        cnt = 0
        for i, j in ((0,0), (1,0), (0,1), (1,1)):
            hi = h + i
            wj = w + j
            if grid[hi][wj] == '#':
                cnt += 1
        if cnt % 2:
            ans += 1
print(ans)