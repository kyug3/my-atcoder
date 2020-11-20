import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
 
N = int(input())
h = list(map(int, input().split()))
dp = [0] + [float('inf')] * (N-1)
 
def rec(i):
    if dp[i] < float('inf'):
        return dp[i]
    if i == 0:
        return 0
    res = float('inf')
    res = min(res, rec(i-1) + abs(h[i] - h[i-1]))
    if i > 1:
        res = min(res, rec(i-2) + abs(h[i] - h[i-2]))
    dp[i] = res
    return dp[i]
 
def main():
    print(rec(N-1))
 
if __name__ == "__main__":
    main()