S = input()
K = int(input())
N = len(S)

if len(set(S)) == 1:
    print((N * K) // 2)
    exit()

if len(set(S)) >= 2 and S[0] == S[-1]:
    x = S[0]
    for i in range(N):
        if S[i] != x:
            l = i
            break
    for i in range(N):
        if S[N-1-i] != x:
            r = i
            break
    S = S[l:-r]
    a = l//2 + r//2 + (K-1) * ((l+r)//2)
else:
    a = 0

cnt = 0
skip = False
for i in range(len(S) - 1):
    if skip:
        skip = False
        continue
    if S[i] == S[i+1]:
        cnt += 1
        skip = True

print(cnt * K + a)