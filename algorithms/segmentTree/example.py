N, K = map(int, input().split())
A = []
for i in range(N):
    A.append(int(input()))

N = 300000
seg = segmentTree(N, op, 0)

for i in A:
    l = min(N, max(0, i - K))
    r = max(0, min(N, i + K))
    v = seg.query(l, r + 1)
    seg.set(i, v + 1)
print(seg.query(0, N))
