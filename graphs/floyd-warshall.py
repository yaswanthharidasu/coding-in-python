def floydWarshall(n, graph):
    # graph is 2D matrix filled with weights between vertices
    for i in range(n):
        graph[i][i] = 0

    for k in range(n):
        for u in range(n):
            for v in range(n):
                if graph[u][k] == float('inf') or graph[k][v] == float('inf'):
                   continue
                graph[u][v] = min(graph[u][v], graph[u][k]+graph[k][v])