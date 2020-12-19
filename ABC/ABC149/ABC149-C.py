import sys
import math
input = sys.stdin.readline

def is_prime(n):
    if n == 1:
        False
    for k in range(2, n + 1):
        if k ** 2 > n:
            break
        if n % k == 0:
            return False
    return True

X = int(input())
while True:
    if is_prime(X):
        print(X)
        break
    X += 1