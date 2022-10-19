def solution(a, edges):
    graph = [set() for _ in range(len(a))]
    degree = [0] * len(a)

    for x, y in edges:
        graph[x].add(y)
        graph[y].add(x)
        degree[x] += 1
        degree[y] += 1

    li = []
    for i in range(len(a)):
        if degree[i] == 1:
            li.append(i)

    answer = 0
    while li:
        x = li.pop()

        if len(graph[x]) != 1:
            if a[x] != 0:
                return -1
            continue
        for v in graph[x]:
            answer += abs(a[x])
            a[v] += a[x]
            a[x] = 0

            degree[v] -= 1
            if degree[v] == 1:
                li.append(v)

        if v in graph[x]:
            graph[x].remove(v)
        if x in graph[v]:
            graph[v].remove(x)

    return answer
