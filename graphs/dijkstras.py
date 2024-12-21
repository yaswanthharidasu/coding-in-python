import heapq
MOD = int(1e9+7)

def dijsktras(n, edges, start):
    graph = [[] for _ in range(n+1)]
    for u,v,wt in edges:
        graph[u].append([v, wt])

    distances = [float('inf') for _ in range(n+1)]
    distances[start] = 0
    shortest = [(0, start)]

    while shortest:
        currDistance, u = heapq.heappop(shortest)
        # To avoid reiterating of neighbours of node u (same node can present two times in the heap)
        if currDistance > distances[u]:
            continue
        for v, wt in graph[u]:
            if currDistance+wt < distances[v]:
                distances[v] = currDistance+wt
                heapq.heappush(shortest, (distances[v], v))

def noOfShortestPaths(n, edges, start):
    graph = [[] for _ in range(n+1)]
    for u,v,wt in edges:
        graph[u].append([v, wt])

    distances = [float('inf') for _ in range(n+1)]
    paths = [0 for _ in range(n+1)]
    distances[start] = 0
    paths[0] = 1
    shortest = [(0, start)]

    while shortest:
        currDistance, u = heapq.heappop(shortest)
        if currDistance > distances[u]:
            continue

        for v, wt in graph[u]:
            if currDistance+wt < distances[v]:
                distances[v] = currDistance+wt
                paths[v] = paths[u]%MOD
                heapq.heappush(shortest, (distances[v], v))
            elif currDistance+wt == distances[v]:
                paths[v] = (paths[v]+paths[u])%MOD
