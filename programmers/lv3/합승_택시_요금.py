def floyd(n, graph):
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[j][i],
                                  graph[i][k] + graph[k][j])
                graph[j][i] = graph[i][j]


def solution(n, s, a, b, fares):
    graph = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        graph[i][i] = 0

    for i, j, k in fares:
        graph[i][j] = k
        graph[i][j] = k

    floyd(n, graph)

    answer = float('inf')
    for i in range(1, n + 1):
        answer = min(answer, graph[a][i] + graph[i][b] + graph[s][i])

    return answer
