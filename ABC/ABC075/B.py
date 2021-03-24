H, W = map(int, input().split())
grid = [
    ['.'] * (W+2) if i == 0 or i == (H+1)
    else ['.'] + list(input()) + ['.']
    for i in range(H+2)
]
ans = [[0] * W for _ in range(H)]
for h in range(1, H+1):
    for w in range(1, W+1):
        if grid[h][w] == '#':
            ans[h-1][w-1] = '#'
            continue
        else:
            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    if grid[h+i][w+j] == '#':
                        ans[h-1][w-1] += 1

for x in ans:
    print(''.join(map(str, x)))