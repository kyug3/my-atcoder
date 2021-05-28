# AOJ ALDS1_14_B

base = 37
mod = 10**9 + 9
pw = None
def rolling_hash(s):
    l = len(s)
    h = [0]*(l + 1)
    v = 0
    for i in range(l):
        h[i+1] = v = (v * base + ord(s[i])) % mod
    return h

def setup_pw(l):
    global pw
    pw = [1]*(l + 1)
    v = 1
    for i in range(l):
        pw[i+1] = v = v * base % mod

def get(h, l, r):
    return (h[r] - h[l] * pw[r-l]) % mod

T = input().rstrip()
P = input().rstrip()

HT = rolling_hash(T)
HP = rolling_hash(P)
lt = len(T)
lp = len(P)
setup_pw(lp)
pv = get(HP, 0, lp)
for i in range(lt - lp + 1):
    if get(HT, i, i+lp) == pv:
        print(i)

