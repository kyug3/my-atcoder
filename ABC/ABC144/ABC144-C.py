import sys
input = sys.stdin.readline

N = int(input())
for n in range(1, N):
    if n * n > N:
        break
    if (N / n).is_integer():
        x = n
        y = N // n    
print(x + y - 2)