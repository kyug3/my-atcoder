import sys, math
sys.setrecursionlimit(1000000)
INF = 1 << 100
#mod = 1000000007
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))

"""
K=Nのとき明らかに1になる
N mod K = (N-K) mod K なので一度割り切れなくなると-Kし続ける
Nを割り切れなくなるまでKで割って、mod K = 1 ならOK
一度も割れない場合、N mod K = 1で、これは(N-1) mod K = 0なので、N-1の約数を数える
割れる場合KはNの倍数なので、全部試せそう
"""

N = int(input())

def get_divisors(x: int) -> list:
    divisors = []
    for i in range(1, x+1):
        if i * i > x:
            break
        if x % i == 0:
            divisors.append(i)
            if x // i != i:
                divisors.append(x // i)
    return divisors
b = len(get_divisors(N-1)) - 1
divs = get_divisors(N)
for i in divs:
    if i == 1:
        continue
    n = N
    while n % i == 0:
        n //= i
    if n % i == 1:
        b += 1
print(b)