import numpy as np

W, H, N = map(int, input().split())
array = np.ones((H, W))
for _ in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        array[:, :x] = 0
    elif a == 2:
        array[:, x:] = 0
    elif a == 3:
        array[:y, :] = 0
    else:
        array[y:, :] = 0

print(int(np.sum(array)))