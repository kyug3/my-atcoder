import sys
import math
input = sys.stdin.readline

A, B, C, D = map(int, input().split())

gcd = math.gcd(C, D)
L = C // gcd * D

def func(x):
    return x - x // C - x // D + x // L

print(func(B) - func(A-1))