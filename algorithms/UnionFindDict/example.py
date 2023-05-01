# コンストラクタに辞書を渡します
class UnionFindDict:
    def __init__(self, s):
        self.n = len(s)
        self.s = s
        self.parents = {i:-1 for i in s}

    def find(self, x):
        if type(self.parents[x])==type(0) and self.parents[x] < 0:
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

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in self.parents  if self.find(i) == root]

    def roots(self):
        return [i for i, x in self.parents.items() if type(x)==type(0) and x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        ret = {}
        for i in self.parents:
            root = self.find(i)
            ret.setdefault(root, [])
            ret[root].append(i)
        return ret

    def __str__(self):
        return "\n".join("{}: {}".format(r, self.members(r)) for r in self.roots())

#ABC300C
H,W=map(int,input().split())
C=[]
for i in range(H):
    C+=list(input()),

s=set()
for i in range(H):
    for j in range(W):
        s.add((i,j))
tree=UnionFindDict(s)

vec=[[1,1],[-1,1],[1,-1],[-1,-1]]
for i in range(H):
    for j in range(W):
        for vy,vx in vec:
            if 0<=i+vy<H and 0<=j+vx<W:
                if C[i][j]==C[i+vy][j+vx]=="#":
                    tree.union((i,j),(i+vy,j+vx))

members=tree.all_group_members()
ans=[0]*min(H,W)
for v in members.values():
    if len(v)>1:
        ans[len(v)//4-1]+=1

print(*ans)
