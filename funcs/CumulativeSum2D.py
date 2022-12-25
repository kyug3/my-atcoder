class CumulativeSum2D:
    # 0-indexedで受け取る
    def __init__(self, h, w):
        self.H = h + 1
        self.W = w + 1
        self.data = [[0] * (w+1) for _ in range(h+1)]

    def build(self):
        for h in range(1, self.H):
            for w in range(1, self.W):
                self.data[h][w] += self.data[h][w-1] + self.data[h-1][w] - self.data[h-1][w-1]

    def add(self, h, w, val):
        self.data[h+1][w+1] += val

    def get(self, h1, w1, h2, w2):
        # 矩形に含まれる左上の点と右下の点の座標
        return self.data[h2+1][w2+1] - self.data[h2+1][w1] - self.data[h1][w2+1] + self.data[h1][w1]
