def fib(x):
    if x <= 1:
        return 1
    elif memo[x]:
        return memo[x]
    ans = fib(x - 1) + fib(x - 2)
    memo[x] = ans
    return ans

n = int(input())
memo = [0] * (n + 1)
print(fib(n))