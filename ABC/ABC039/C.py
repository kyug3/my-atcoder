import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
def li(): return list(map(int, input().split()))

S = input()

onkai = {
    'WBWBWWBWBWBW': 'Do',
    'WBWWBWBWBWWB': 'Re',
    'WWBWBWBWWBWB': 'Mi',
    'WBWBWBWWBWBW': 'Fa',
    'WBWBWWBWBWWB': 'So',
    'WBWWBWBWWBWB': 'La',
    'WWBWBWWBWBWB': 'Si',
}
print(onkai[S[:12]])