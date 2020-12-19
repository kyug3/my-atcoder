S = input()
N = len(S)
S2 = S[:(N - 1) // 2]
S3 = S[(N + 3) // 2 - 1:]

def func(x):
    lx = len(x)
    if lx % 2 == 1 and x[:lx // 2] == x[lx // 2 + 1:][::-1]:
        return True
    elif x[:lx // 2] == x[lx // 2:][::-1]:
        return True
    return False

if func(S) and func(S2) and func(S3):
    print("Yes")
else:
    print("No")