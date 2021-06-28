import sys, math
sys.setrecursionlimit(10**9)
mod = 10**9 + 7
#mod = 998244353
input = sys.stdin.readline
def li(): return list(map(int, input().split()))

N, K = li()
A = li()
ma = max(max(A), K)
for i in range(100):
    if 2 ** i > ma:
        digit = i
        break

lst = [0] * digit
x = 0
for i in range(N):
    b = bin(A[i])
    b = b[2:][::-1]
    for j in range(digit):
        try:
            if b[j] == '1':
                lst[j] += 1
            else:
                lst[j] -= 1
        except:
            lst[j] -= 1

for i in range(100):
    if 2 ** i > K:
        x_digit = i
        break

count = 0
l = []
for i in range(x_digit)[::-1]:
    if lst[i] < 0 and count + 2 ** i <= K:
        l.append('1')
        count  += 2 ** i
    else:
        l.append('0')

if not l:
    l.append('0')
x = int(''.join(l), 2)

ans = 0
for i in range(N):
    ans += x ^ A[i]
print(ans)
