import sys, math
sys.setrecursionlimit(1000000)
INF = 1 << 100
#mod = 1000000007
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))

def add(idx):
    # idxを区間に加えるときの処理
    global val
    a = A[idx]
    cnt[a] += 1
    if cnt[a] & 1:
        val += 1
    else:
        val -= 1

def erase(idx):
    # idxを区間から消すときの処理
    global val
    a = A[idx]
    cnt[a] -= 1
    if cnt[a] & 1:
        val += 1
    else:
        val -= 1


N = int(input())
B = int(math.sqrt(N)) + 1
A = li()
Q = int(input())
query = [[] for _ in range(B+1)]
for i in range(Q):
    l, r = li()
    l -= 1; r -= 1
    query[r//B].append((l, r, i))

# ジグザグにソート
for i in range(B+1):
    if i & 1:
        query[i].sort(key=lambda x: -x[0])
    else:
        query[i].sort(key=lambda x: x[0])

nl = 0; nr = 0
cnt = [0] * (N+1)
val = 0
out = [0] * Q

for q in query:
    for l, r, i in q:
        while r >= nr: # rまでの区間を増やす
            add(nr)
            nr += 1
        while r + 1 < nr: # rまで区間を消す
            nr -= 1
            erase(nr)
        while l  > nl: # lまで区間を消す
            erase(nl)
            nl += 1
        while l < nl: # lまで区間を増やす
            nl -= 1
            add(nl)
        out[i] = (r-l+1-val) // 2

print(*out, sep='\n')
