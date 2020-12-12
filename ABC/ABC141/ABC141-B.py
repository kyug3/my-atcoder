import sys
input = sys.stdin.readline

S = input().rstrip()
for n in range(len(S)):
    if (n + 1) % 2:
        if S[n] == "L":
            print("No")
            break
    elif S[n] == "R":
        print("No")
        break
else:
    print("Yes")