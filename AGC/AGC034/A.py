N, A, B, C, D = map(int, input().split())
S = input()[A-1 : max(C,D)]
N = len(S)
B -= A; C -= A; D -= A; A = 0

for i in range(1, N):
    if S[i] == S[i-1] == '#':
        print('No')
        exit()
if C < D:
    print('Yes')
    exit()

for i in range(B+1, D+2):
    if S[i] == S[i-1] == S[i-2] == '.':
        print('Yes')
        exit()
print('No')