from itertools import groupby

def RLE(s: str) -> list:
    encoded = []
    for key, group in groupby(s):
        encoded.append([key, len(list(group))])
    return encoded

X = input()
N = len(X)
X = RLE(X)
ans = 0
rest_S = 0
for i in range(len(X) - 1):
    if X[i][0] == 'S':
        rest_S += X[i][1]
        now_T = X[i+1][1]
        if now_T >= rest_S:
            ans += 2 * rest_S
            rest_S = 0
        else:
            ans += 2 * now_T
            rest_S -= now_T

print(N - ans)
