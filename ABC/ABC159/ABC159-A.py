N, M = map(int, input().split())
def func(x):
    return (x - 1) * x // 2

print(func(N) + func(M))