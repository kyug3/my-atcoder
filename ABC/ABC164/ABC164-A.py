import sys
input = sys.stdin.readline

S, W = map(int, input().split())
if W >= S:
    print('unsafe')
else:
    print('safe')