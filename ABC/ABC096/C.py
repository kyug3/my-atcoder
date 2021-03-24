H, W = map(int, input().split())
grid = [['.'] * (W+2) if i == 0 or i == H+1 else ['.'] + list(input()) + ['.'] for i in range(H + 2)]

for h in range(H):
    for w in range(W):
        if grid[h][w] == '.':
            continue
        ok = False
        if (grid[h+1][w] == '#' or grid[h-1][w] == '#'
            or grid[h][w+1] == '#' or grid[h][w-1] == '#'):
            ok = True
        if not ok:
            print('No')
            exit()
else:
    print('Yes')