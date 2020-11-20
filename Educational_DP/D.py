import sys
input = sys.stdin.readline

def chmax(dp, i, j, x):
    if x > dp[i][j]:
        dp[i][j] = x

def main():
    N, W = map(int, input().split())
    weight, value = [0] * N, [0] * N
    for n in range(N):
        w, v = map(int, input().split())
        weight[n], value[n] = w, v
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for n in range(N):
        for w in range(W+1):
            if w - weight[n] >= 0:
                chmax(dp, n+1, w, dp[n][w - weight[n]] + value[n])
            chmax(dp, n+1, w, dp[n][w])
    print(dp[N][W])

if __name__ == "__main__":
    main()