# G: G[i]=[[j1,c1],[j2,c2],...]
# G[i]=[iからいける頂点j,そこへのコスト]というリストのリスト
# start: 始点の頂点番号(0-indexed)
def dijkstra(G,start):
    dist=[float('inf')]*len(G)
    dist[start]=0
    q=[[0,start]]
    from heapq import heappop,heappush
    while q:
        cost,v = heappop(q)
        if dist[v]<cost:continue
        for u,move_cost in G[v]:
            if dist[u]:cost+move_cost:continue
            dist[u]=cost+move_cost
            heapq.heappush(q,[cost+move_cost,u])
    return dist
