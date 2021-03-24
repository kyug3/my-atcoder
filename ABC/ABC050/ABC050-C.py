N = int(input())
frag = True if N % 2 == 1 else False
A = list(map(int, input().split()))
mod = 10 ** 9 + 7
bucket = [0] * N
for a in A:
    bucket[a] += 1

x = 2 if frag else 1
if frag and bucket[0] != 1:
    print(0)
    exit()
for i in range(x, N, 2):
    if bucket[i] != 2:
        print(0)
        break
else:
    print(2 ** (N // 2) % mod)