import sys
input = sys.stdin.readline

N = int(input())
SP = [input().rstrip().split() + [n+1] for n in range(N)]

def func(x):
    x[1] = int(x[1]) * -1
    return (x[0], x[1]) 

SP.sort(key=func)
for n in range(N):
    print(SP[n][2])