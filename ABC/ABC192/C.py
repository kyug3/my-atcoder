N, K = map(int, input().split())

def func(x):
    x = str(x)
    g1 = sorted(x, reverse=True)
    g2 = sorted(x)
    return int(''.join(g1)) - int(''.join(g2))

for i in range(K):
    N = func(N)
print(N)