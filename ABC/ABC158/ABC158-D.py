import sys
from collections import deque
input = sys.stdin.readline

S = deque(list(input().rstrip()))
Q = int(input())

rev = 0
for _ in range(Q):
    q = list(input().rstrip().split())
    if q[0] == '1':
        rev += 1
    else:
        if rev % 2 == 0:
            if q[1] == '1':
                S.appendleft(q[2])
            else:
                S.append(q[2])
        else:
            if q[1] == '2':
                S.appendleft(q[2])
            else:
                S.append(q[2])
S = list(S)
if rev % 2 == 1:
    S = S[::-1]
print(''.join(S))