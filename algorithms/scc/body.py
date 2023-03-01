# 参考
# https://tjkendev.github.io/procon-library/python/graph/scc.html
# 上記コードを非再帰に変更したもの
# 強連結成分分解(SCC): グラフGに対するSCCを行う
# 入力: <N>: 頂点サイズ, <G>: 順方向の有向グラフ, <RG>: 逆方向の有向グラフ
# 出力: (<ラベル数>, <各頂点のラベル番号>)
def scc(N, G, RG):
    order = []
    used = [0] * N
    group = [None] * N
    import copy

    G2 = copy.deepcopy(G)
    stack = []

    def dfs(stack):
        while stack:
            v = stack[-1]
            used[v] = 1
            haveChild = False
            while G2[v]:
                u = G2[v].pop()
                if used[u]:
                    continue
                stack += (u,)
                haveChild = True
                break
            if not haveChild:
                order.append(stack.pop())

    def rdfs(s, col):
        group[s] = col
        used[s] = 1
        stack = [s]
        while stack:
            v = stack.pop()
            for t in RG[v]:
                if not used[t]:
                    group[t] = col
                    stack += (t,)
                    used[t] = 1

    for i in range(N):
        if not used[i]:
            dfs([i])
    used = [0] * N
    label = 0
    for s in reversed(order):
        if not used[s]:
            rdfs(s, label)
            label += 1
    return label, group


# 縮約後のグラフを構築
def construct(N, G, label, group):
    G0 = [set() for i in range(label)]
    GP = [[] for i in range(label)]
    for v in range(N):
        lbs = group[v]
        for w in G[v]:
            lbt = group[w]
            if lbs == lbt:
                continue
            G0[lbs].add(lbt)
        GP[lbs].append(v)
    return G0, GP


