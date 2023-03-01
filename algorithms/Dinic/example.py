def abc259g():
    H, W = map(int, input().split())
    f = []
    for i in range(H):
        f += (list(map(int, input().split())),)

    dinic = Dinic(H + W + 2)

    base = 0
    for i in range(H):
        s, a = 0, 0
        for j in f[i]:
            s += abs(j)
            a += j
        base += s
        # 選ばない
        dinic.add_edge(0, i + 1, s)
        # 選ぶ
        dinic.add_edge(i + 1, H + W + 1, s - a)

    for i in range(W):
        s, a = 0, 0
        for j in range(H):
            j = f[j][i]
            s += abs(j)
            a += j
        base += s
        # 選ぶ
        dinic.add_edge(0, H + i + 1, s - a)
        # 選ばない
        dinic.add_edge(H + i + 1, H + W + 1, s)

    for i in range(H):
        for j in range(W):
            if f[i][j] < 0:
                dinic.add_edge(i + 1, H + j + 1, 10 ** 18)
            else:
                dinic.add_edge(i + 1, H + j + 1, f[i][j])

    print(base - dinic.flow(0, H + W + 1))


abc259g()
