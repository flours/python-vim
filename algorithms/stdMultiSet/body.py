def binarySearch(X, target, left, right):
    while True:
        mid = (left + right) // 2
        if X[left] > target:
            return left
        if X[right] <= target:
            return right
        if left == right:
            return left
        if X[mid] > target:
            right = mid - 1
        else:
            left = mid
            right = right - 1


class stdMultiSet:
    def __init__(self, valueList):
        valueList += (min(valueList) - 1, max(valueList) + 1)
        self.size = 1 << len(set(valueList)).bit_length()
        self.tree = [0] * (self.size + 1)
        self.valueSet = set(valueList)
        self.sortedValueList = sorted(list(set(valueList)))
        self.value2Idx = {v: i + 1 for i, v in enumerate(sorted(list(set(valueList))))}
        self.idx2Value = {i + 1: v for i, v in enumerate(sorted(list(set(valueList))))}
        self.length = 0

    # i番目の値を検索
    def __getitem__(self, key):
        if key > self.__len__() or key <= 0:
            raise "index out of range" + str(key)
        value = 0
        idx = 1 << (self.size.bit_length()) - 1
        width = idx // 2
        while width:
            if key <= value + self.tree[idx]:
                idx -= width
            else:
                value += self.tree[idx]
                idx += width
            width //= 2
        if key <= value + self.tree[idx]:
            return self.idx2Value[idx]
        else:
            return self.idx2Value[idx + 1]

    def __len__(self):
        return self.length

    def __sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    # upper_bound(x) xより大きい最小のインデックス
    # 最大値より大きい場合は最大のインデックスを返す
    def upper_bound(self, i):
        return self.lower_bound(i + 1)

    # lower_bound(x) x以上の最小のインデックス
    # 最大値より大きい場合は最大のインデックスを返す
    def lower_bound(self, i):
        # 座圧のどのインデックスに対応するか確認
        idx = min(
            binarySearch(self.sortedValueList, i - 1, 0, len(self.sortedValueList) - 1)
            + 1,
            self.size,
        )
        # idx以下の数字の個数(つまりインデックス)を求める
        value = self.__sum(idx)
        return min(value + 1, self.length)

    # iを削除
    def remove(self, i):
        i = self.value2Idx[i]
        x = -1
        self.length -= 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    # iを追加
    def add(self, i):
        i = self.value2Idx[i]
        x = 1
        self.length += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def __str__(self):
        s = []
        for i in range(self.__len__()):
            s += (self.__getitem__(i + 1),)
        return str(s)
:
