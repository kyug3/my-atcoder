import sys
input = sys.stdin.readline

a, b = input().split()

if a == 'H':
    print(b)
else:
    print('H' if b == 'D' else 'D')