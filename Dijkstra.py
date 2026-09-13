import heapq

n = 100
goal = 5

def dijkstra(graph, start):
    INF = float('inf')
    dist = [INF]*(n+1)
    dist[start] = 0
    heap = [[0, start]]

    while heap:
        d, node = heapq.heappop(heap)

        if d != dist[node]:
            continue

        if node == goal:
            print(d)
            break

        for nxt, w in graph[node]:
            nd = d + w
            if nd < dist[nxt]:
                dist[nxt] = nd
                heapq.heappush(heap, (nd, nxt))