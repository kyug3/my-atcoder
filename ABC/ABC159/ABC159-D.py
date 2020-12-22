N = int(input())
A = list(map(int, input().split()))

def comb(n):
    return (n * (n - 1)) // 2

bucket = [0 for _ in range(N + 1)]
for a in A:
    bucket[a] += 1

SUM = 0
for b in bucket:
    if b >= 2:
        SUM += comb(b)
        
ans = 0
for a in A:
    x = bucket[a]
    if x >= 2:
        ans = SUM - comb(x) + comb(x - 1)
    else:
        ans = SUM
    print(ans)
