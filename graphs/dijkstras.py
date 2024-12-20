import heapq

def dijsktras(n, edges, start):
    graph = [[] for _ in range(n+1)]
    for u,v,w in edges:
        graph[u].append([v, w])

    distances = [float('inf') for _ in range(n+1)]
    distances[start] = 0
    shortest = [(0, start)]

    while len(shortest) != 0:
        currDistance, u = heapq.heappop(shortest)
        # To avoid reiterating of neighbours of node u (same node can present two times in the heap)
        if currDistance > distances[u]:
            continue
        for v, w in graph[u]:
            if distances[u]+w < distances[v]:
                distances[v] = distances[u]+w
                heapq.heappush(shortest, [distances[v], v])
