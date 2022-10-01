class StringHash:
    def __init__(self, string, base=37, mod=1000000009):
        self.string = string
        self.l = len(string)
        self.base = base
        self.mod = mod
        self.hash = self._string_hash()
        self.pw = self._setup_pw()

    def _string_hash(self):
        hash = [0] * (self.l + 1)
        v = 0
        for i in range(self.l):
            hash[i+1] = v = (v * self.base + ord(self.string[i])) % self.mod
        return hash

    def _setup_pw(self):
        pw = [1] * (self.l + 1)
        v = 1
        for i in range(self.l):
            pw[i+1] = v = v * self.base % self.mod
        return pw

    def get(self, l, r):
        "get [l, r)"
        return (self.hash[r] - self.hash[l] * self.pw[r-l]) % self.mod
    