from body import UnionFind

if __name__ == "__main__":
    tree = UnionFind(len(arr))
    tree.union(0, 3)
    tree.union(0, 4)
    tree.union(4, len(arr) - 1)
    tree.union(1, 2)
    tree.union(1, 5)
    tree.union(5, 6)
    tree.union(7, 6)
    tree.union(8, 9)
    tree.union(9, 10)
    tree.union(10, 11)
    tree.union(11, 12)
    print(tree.all_group_members())
