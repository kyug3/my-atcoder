import numpy as np

N = int(input())
A = np.array(input().split(), np.int64)
u, counts = np.unique(A, return_counts=True)
u = u[::-1]; counts = counts[::-1]

x, y = 0, 0
for i in range(N):
    c = counts[i]
    if c >= 2:
        if not x:
            if c >= 4:
                x, y = u[i], u[i]
                print(x * y)
                break
            else:
                x = u[i]
        else:
            y = u[i]
            print(x * y)
            break
else:
    print(0)
