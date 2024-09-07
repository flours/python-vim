class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.right = list(range(n))
        self.left = list(range(n))

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x
        max_v=max(self.right[x],self.right[y])
        min_v=min(self.left[x],self.left[y])

        self.parents[x] += self.parents[y]
        self.parents[y] = x

        self.right[x]=max_v
        self.left[x]=min_v
    def find_right(self,x):
        return self.right[self.find(x)]

    def find_left(self,x):
        return self.left[self.find(x)]


    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        ret = {}
        for i in range(self.n):
            root = self.find(i)
            ret.setdefault(root, [])
            ret[root].append(i)
        return ret

    def __str__(self):
        return "\n".join("{}: {}".format(r, self.members(r)) for r in self.roots())


