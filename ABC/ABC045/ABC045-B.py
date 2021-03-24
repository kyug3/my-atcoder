from collections import deque
A = deque(input())
B = deque(input())
C = deque(input())

turn = 'a'
while True:
    if turn == 'a':
        if not A:
            print('A')
            break
        turn = A.popleft()
    elif turn == 'b':
        if not B:
            print('B')
            break
        turn = B.popleft()
    else:
        if not C:
            print('C')
            break
        turn = C.popleft()
