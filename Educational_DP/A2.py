import sys
input = sys.stdin.readline

def chmin(dp, i, x):
    if x < dp[i]:
        dp[i] = x

def main():
    N = int(input())
    h = list(map(int, input().split()))
    dp = [0] + [float('inf')] * (N - 1)
    for i in range(1, N):
        chmin(dp, i, dp[i-1] + abs(h[i] - h[i-1]))
        if i > 1:
            chmin(dp, i, dp[i-2] + abs(h[i] - h[i-2]))
    print(dp[-1])

if __name__ == "__main__":
    main()