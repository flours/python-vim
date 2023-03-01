def op(a, b):
    return max(a, b)


class segmentTree:
    def __init__(self, n, op, init_value):
        dataLen = 1 << (n - 1).bit_length()
        self.data = [init_value] * (2 * dataLen)
        self.op = op
        self.length = dataLen

    def getIdx(self, left, right):
        idxs = []
        l = left
        r = right
        while True:
            idx = 1
            valueL = 0
            valueR = self.length - 1
            while l != valueL or valueR >= r:
                if l <= (valueR + valueL) >> 1:
                    valueR -= (valueR - valueL + 1) >> 1
                    idx <<= 1
                else:
                    valueL += (valueR - valueL + 1) >> 1
                    idx = idx * 2 + 1
            idxs.append(idx)
            if valueR == r - 1:
                break
            l = valueR + 1
        return idxs

    def get(self, n):
        return self.data[n + self.length]

    def set(self, n, value):
        idx1 = n + self.length
        self.data[idx1] = value
        while idx1 != 1:
            idx2 = idx1 ^ 1
            if idx1 > idx2:
                idx1, idx2 = idx2, idx1
            self.data[idx1 >> 1] = self.op(self.data[idx1], self.data[idx2])
            idx1 >>= 1

    def query(self, l, r):
        idxs = self.getIdx(l, r)
        ret = self.data[idxs[0]]
        for idx in idxs:
            ret = self.op(ret, self.data[idx])
        return ret
