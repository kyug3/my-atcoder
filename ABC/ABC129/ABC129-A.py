import sys
input = sys.stdin.readline

P, Q, R = map(int, input().split())
print(min(P+Q, min(Q+R, R+P)))