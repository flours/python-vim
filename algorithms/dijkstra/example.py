N,A,B,C=map(int,input().split())

# 0~N-1は自家用車移動、N~2*N-1は電車移動
G=[[] for i in range(N*2)]

for i in range(N):
    x=list(map(int,input().split()))
    G[i]+=[i+N,0],
    for j in range(N):
        if i!=j:
            G[i]+=[j,x[j]*A],
            G[i+N]+=[j+N,x[j]*B+C],

dist=dijkstra(G,0)
print(dist[2*N-1])

