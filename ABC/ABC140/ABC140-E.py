# https://github.com/tatyam-prime/SortedSet/blob/main/SortedSet.py
from math import sqrt, ceil
from bisect import bisect_left, bisect_right
from typing import Iterable, TypeVar, Union, Tuple
T = TypeVar('T')

class SortedSet:
	BUCKET_RATIO = 50
	REBUILD_RATIO = 170

	@classmethod
	def _new_bucket_size(cls, size: int) -> int:
		return int(ceil(sqrt(size / cls.BUCKET_RATIO)))

	def _build(self, a: list):
		size = self.size = len(a)
		bucket_size = self._new_bucket_size(self.size)
		self.a = [a[size * i // bucket_size : size * (i + 1) // bucket_size] for i in range(bucket_size)]
	
	def __init__(self, a: Iterable = []):
		"Make a new SortedSet from iterable. / O(N) if sorted and unique / O(N log N)"
		a = list(a)
		if not all(a[i] < a[i + 1] for i in range(len(a) - 1)):
			a = sorted(set(a))
		self._build(a)

	def __iter__(self):
		for i in self.a:
			for j in i: yield j

	def __reversed__(self):
		for i in reversed(self.a):
			for j in reversed(i): yield j
	
	def __len__(self) -> int:
		return self.size
	
	def __repr__(self) -> str:
		return str(self.a)
	
	def __str__(self) -> str:
		s = str(list(self))
		return "{" + s[1 : len(s) - 1] + "}"

	def _bucket_index(self, x: T) -> int:
		"Find the index of the bucket which should contain x. / O(log N)"
		ok = -1
		ng = len(self.a)
		a = self.a
		while ng - ok > 1:
			mid = (ng + ok) >> 1
			if a[mid][0] <= x: ok = mid
			else: ng = mid
		if ok == -1: return 0
		if ng == len(self.a): return ok
		if a[ok][-1] < x:
			return ok + (len(a[ok]) > len(a[ok + 1]))
		return ok

	def __contains__(self, x: T) -> bool:
		"O(log N)"
		if self.size == 0: return False
		a = self.a[self._bucket_index(x)]
		i = bisect_left(a, x)
		return i != len(a) and a[i] == x

	def add(self, x: T) -> bool:
		"Add an element and return True if added. / O(N ** 0.5)"
		if self.size == 0:
			self._build([x])
			return True
		a = self.a[self._bucket_index(x)]
		i = bisect_left(a, x)
		if i != len(a) and a[i] == x: return False
		a.insert(i, x)
		self.size += 1
		if len(a) > len(self.a) * self.REBUILD_RATIO:
			self._build(list(self))
		return True

	def discard(self, x: T) -> bool:
		"Remove an element and return True if removed. / O(N ** 0.5)"
		if self.size == 0: return False
		a = self.a[self._bucket_index(x)]
		i = bisect_left(a, x)
		if i == len(a) or a[i] != x: return False
		a.pop(i)
		self.size -= 1
		if len(a) == 0:
			self._build(list(self))
		return True
	
	def lt(self, x: T) -> Union[T, None]:
		"Return the largest element < x, or None if it doesn't exist. / O(log N)"
		if self.size == 0: return None
		i = self._bucket_index(x)
		a = self.a
		if a[i][0] >= x:
			return a[i - 1][-1] if i else None
		return a[i][bisect_left(a[i], x) - 1]

	def le(self, x: T) -> Union[T, None]:
		"Return the largest element <= x, or None if it doesn't exist. / O(log N)"
		if self.size == 0: return None
		i = self._bucket_index(x)
		a = self.a
		if a[i][0] > x:
			return a[i - 1][-1] if i else None
		return a[i][bisect_right(a[i], x) - 1]

	def gt(self, x: T) -> Union[T, None]:
		"Return the smallest element > x, or None if it doesn't exist. / O(log N)"
		if self.size == 0: return None
		i = self._bucket_index(x)
		a = self.a
		if a[i][-1] <= x:
			return a[i + 1][0] if i + 1 < len(self.a) else None
		return a[i][bisect_right(a[i], x)]

	def ge(self, x: T) -> Union[T, None]:
		"Return the smallest element >= x, or None if it doesn't exist. / O(log N)"
		if self.size == 0: return None
		i = self._bucket_index(x)
		a = self.a
		if a[i][-1] < x:
			return a[i + 1][0] if i + 1 < len(self.a) else None
		return a[i][bisect_left(a[i], x)]
	
	def __getitem__(self, x: int) -> T:
		"Take (i, j) and return the j-th element in the i-th bucket, or IndexError if it doesn't exist. / O(1)"
		"Take x and return the x-th element, or IndexError if it doesn't exist. / O(N ** 0.5) (fast)"
		if isinstance(x, tuple):
			return self.a[x[0]][x[1]]
		if x < 0: x += self.size
		if x < 0 or x >= self.size: raise IndexError
		for a in self.a:
			if x < len(a): return a[x]
			x -= len(a)
		assert False
	
	def index(self, x: T) -> int:
		"Return the index of x, or ValueError if it doesn't exist. / O(N ** 0.5) (fast)"
		if self.size == 0: raise ValueError
		idx = self._bucket_index(x)
		a = self.a[idx]
		i = bisect_left(a, x)
		if i == len(a) or a[i] != x: raise ValueError
		for j in range(idx): i += len(self.a[j])
		return i

	def lower_bound(self, x: T) -> Tuple[int, int]:
		"Find the smallest element self.a[i][j] >= x and return (i, j), or (len(a), 0) if it doesn't exist. / O(log N)"
		if self.size == 0:
			return (0, 0)
		i = self._bucket_index(x)
		a = self.a
		if a[i][-1] < x:
			return (i + 1, 0)
		return (i, bisect_left(a[i], x))

	def upper_bound(self, x: T) -> Tuple[int, int]:
		"Find the smallest element self.a[i][j] > x and return (i, j), or (len(a), 0) if it doesn't exist. / O(log N)"
		if self.size == 0:
			return (0, 0)
		i = self._bucket_index(x)
		a = self.a
		if a[i][-1] <= x:
			return (i + 1, 0)
		return (i, bisect_right(a[i], x))

import sys, math
sys.setrecursionlimit(10**6)
INF = float('inf')
mod = 10**9 + 7
#mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))


N = int(input())
P = li()
dic = {p: e for e, p in enumerate(P)}
sorted_P = sorted(P, reverse=True)
ans = 0
se = SortedSet([-2,-1, N, N+1])

for i in range(N):
    p = sorted_P[i]
    idx = dic[p]
    r1 = se.gt(idx)
    r2 = min(N, se.gt(r1))
    l1 = se.lt(idx)
    l2 = max(-1, se.lt(l1))
    ans += p * (r1 - idx) * (l1 - l2)
    ans += p * (idx - l1) * (r2 - r1)
    se.add(idx)

print(ans)