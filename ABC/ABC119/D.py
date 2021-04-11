A, B, Q = map(int, input().split())
S = [0, 0, 10**11, 10**11]
T = [0, 0, 10**11, 10**11]

def min_dist(n, sw, se, tw, te):
    if sw >= 1 and tw >= 1:
        a = abs(n - min(sw, tw))
    else: a = 10**11
    
    if te <= 10**10 and se <= 10**10:
        b = abs(n - max(te, se))
    else: b = 10**11

    if sw >= 1 and te <= 10**10:
        if abs(n-sw) > abs(n-te):
            sw, te = te, sw
        c = abs(n - sw) + abs(sw - te)
    else: c = 10**11

    if se <= 10**10 and tw >= 1:
        if abs(n-se) > abs(n-tw):
            se, tw = tw, se
        d = abs(n - se) + abs(se - tw)
    else: d = 10**11

    return min((a,b,c,d))



def is_ok(idx, key, lst):
    if lst[idx] >= key:
        return True, lst[idx-1], lst[idx]
    else:
        return False, lst[idx], lst[idx+1]

def binary_search(key, lst):
    ng = -1
    ok = len(lst)
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        tf, a, b = is_ok(mid, key, lst)
        if tf:
            ok = mid
        else:
            ng = mid
    return a, b

for _ in range(A):
    S.append(int(input()))
for _ in range(B):
    T.append(int(input()))
S.sort()
T.sort()

for _ in range(Q):
    x = int(input())
    sw, se = binary_search(x, S)
    tw, te = binary_search(x, T)
    print(min_dist(x, sw, se, tw, te))
