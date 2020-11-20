# code 5.1
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    h = list(map(int, input().split()))
    dp = [0] * N
    for i in range(1, N):
        if i == 1:
            dp[i] = abs(h[i] - h[i-1])
        else:
            dp[i] = min(dp[i-1] + abs(h[i] - h[i-1]),
                        dp[i-2] + abs(h[i] - h[i-2]))
    print(dp[-1])

if __name__ == "__main__":
    main()