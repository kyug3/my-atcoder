import sys
input = sys.stdin.readline

K, X = map(int, input().split())
start = X - K + 1
end = X + K - 1
ans = [str(n) for n in range(start, end + 1)]
print(' '.join(ans))