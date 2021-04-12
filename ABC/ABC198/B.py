N = input()
N = N[::-1]
for i in range(len(N)):
    if N[i] != '0':
        N = N[i:]
        break

print('Yes' if N == N[::-1] else 'No')