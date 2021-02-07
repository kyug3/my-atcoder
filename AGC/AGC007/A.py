H, W = map(int, input().split())
grid = [['.'] * W]
for _ in range(H):
    grid.append(list(input()))

for h in range(1, H+1):
    for w in range(W-1):
        if grid[h][w] == '#' and grid[h-1][w+1] == '#':
            print('Impossible')
            exit()
print('Possible')