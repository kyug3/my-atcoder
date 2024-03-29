def min_factors(N):
    N += 1
    min_fact = [i for i in range(N)]
    min_fact[0] = min_fact[1] = -1
    for i in range(2, N):
        if not min_fact[i] == i:
             continue
        for j in range(i, N, i):
            if min_fact[j] == j:
                min_fact[j] = i
    return min_fact

def factorization(x, min_fact):
    ret = []
    while x > 1:
        ret.append(min_fact[x])
        x //= min_fact[x]
    return ret


from collections import defaultdict
def factorization(x, min_fact):
    dic = defaultdict(int)
    while x > 1:
        dic[min_fact[x]] += 1
        x //= min_fact[x]
    ret = [(i, j) for i, j in dic.items()]
    return ret


"""
def factorization(x):
    lst = []
    if x == 1:
        return lst
    
    # 何度も回す場合、範囲を素数のみにするといいかも
    for n in range(2, x + 1):
        if n * n > x or x == 1:
            break
        count = 0
        while x % n == 0:
            x //= n
            count += 1
        if count:
            lst.append((n, count))

    if x > 1:
        lst.append((x, 1))

    return lst

factorization(24) 
"""
## [(2, 3), (3, 1)] 
##  24 = 2^3 * 3^1