import sys
input = sys.stdin.readline

r, D, x = map(int, input().split())

def func(x):
    return r * x - D

for _ in range(10):
    x = func(x)
    print(x)