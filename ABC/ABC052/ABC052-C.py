N = int(input())
mod = 10** 9 + 7

def factrization(x):
    lst = []
    for i in range(2, x+1):
        cnt = 0
        while True:
            if x % i != 0:
                break
            x //= i
            cnt += 1
        if cnt:
            lst.append((i, cnt))
    return lst

ans = 1
bucket = [0] * (10**5)
for i in range(2, N+1):
    l = factrization(i)
    for j, k in l:
        bucket[j] += k

for x in bucket:
    ans *= (x+1)
    ans %= mod

print(ans)