import sys
input = sys.stdin.readline

S = input().rstrip()
if S[0] == "S":
    if S[1] == "U":
        print(7)
    else:
        print(1)
elif S[0] == "M":
    print(6)
elif S[0] == "T":
    if S[1] == "U":
        print(5)
    else:
        print(3)
elif S[0] == "W":
    print(4)
else:
    print(2)