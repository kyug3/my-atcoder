N = int(input())
S = input()
rgb = [0] * 3
for s in S:
    if s == 'R': rgb[0] += 1
    elif s == 'G': rgb[1] += 1
    else: rgb[2] += 1

x = rgb[0] * rgb[1] * rgb[2]
minus = 0
for i in range(N - 2):
    for j in range(i, N - 1):
        k = j + (j - i)
        if k >= N:
            break
        if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
            minus += 1

print(x - minus)