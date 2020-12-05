import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = input().rstrip()

s = S[K-1].lower()
print(S[:K-1] + s + S[K:])