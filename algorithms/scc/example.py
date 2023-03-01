# ABC245F
def ABC245F():
    N, M = list(map(int, input().split()))
    G = [[] for i in range(N)]
    RG = [[] for i in range(N)]

    for i in range(M):
        a, b = map(lambda x: int(x) - 1, input().split())
        G[a] += [b]
        RG[b] += [a]

    label, group = scc(N, G, RG)
    G0, GP = construct(N, G, label, group)

    seen = [False] * N
    ans = [False] * N
    for i in GP:
        if len(i) != 1:
            for j in i:
                ans[j] = True
                seen[j] = True
    stack = []

    def dfs(v):
        stack = [v]
        while stack:
            v = stack.pop()
            seen[v] = True
            haveChild = False
            while G[v]:
                u = G[v].pop()
                if ans[u]:
                    ans[v] = True
                if seen[u]:
                    continue
                stack += (v,)
                stack += (u,)
                haveChild = True
                break
            # 親がいて自分がTrueなら帰りがけに親に伝播
            if not haveChild and ans[v] and len(stack) > 0:
                ans[stack[-1]] = True

    for i in range(N):
        if seen[i]:
            continue
        dfs(i)
    print(sum(ans))


ABC245F()
