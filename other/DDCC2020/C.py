H, W, K = map(int, input().split())
grid = [list(input()) for _ in range(H)]

ans = [[-1] * W for _ in range(H)]
now = 0
for h in range(H):
    flag = False
    for w in range(W):
        if grid[h][w] == '#':
            now += 1
            if not flag:
                ans[h][:w] = [now] * w
            flag = True
        if flag:
            ans[h][w] = now

for h in range(H):
    if ans[h][0] == -1:
        for i in range(h+1, H):
            if ans[i][0] != -1:
                ans[h:i] = [ans[i] for _ in range(i-h)]
                break
        else:
            ans[h:] = [ans[h-1] for _ in range(H-h)]
            
for x in ans:
    print(*x)