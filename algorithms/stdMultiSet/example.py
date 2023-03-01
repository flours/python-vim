def ABC217D():
    L, Q = map(int, input().split())
    l = [0, L]
    queries = []
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            l += (x,)
        queries += ((c, x),)

    multiSet = stdMultiSet(l)  # 使用する可能性のある数値を入れて初期化
    multiSet.add(0)
    multiSet.add(L)

    for c, x in queries:
        if c == 1:
            multiSet.add(x)
        else:
            idx = multiSet.lower_bound(x)
            print(multiSet[idx] - multiSet[idx - 1])


def ABC241D():
    Q = int(input())
    queries = []
    l = []
    for i in range(Q):
        q = list(map(int, input().split()))
        queries += (q,)
        l += (q[1],)

    multiSet = stdMultiSet(l)

    for q in queries:
        if q[0] == 1:
            multiSet.add(q[1])
        if q[0] == 2:
            if len(multiSet) == 0:
                print(-1)
                continue
            idx = multiSet.upper_bound(q[1])
            idx -= q[2]
            if q[1] + 1 > multiSet[len(multiSet)]:
                idx += 1
            if 0 < idx <= len(multiSet):
                print(multiSet[idx])
            else:
                print(-1)
        if q[0] == 3:
            if len(multiSet) == 0:
                print(-1)
                continue
            idx = multiSet.lower_bound(q[1])
            idx += q[2] - 1
            if q[1] > multiSet[len(multiSet)]:
                idx += 1
            if 0 < idx <= len(multiSet):
                print(multiSet[idx])
            else:
                print(-1)
