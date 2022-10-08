def solution(n, results):

    graph = [[set(), set()] for _ in range(n + 1)]

    for a, b in results:
        graph[a][1].add(b)
        graph[b][0].add(a)

    flag = True
    while flag:
        flag = False
        for a, b in results:
            prev = len(graph[a][1])
            graph[a][1].update(graph[b][1])
            if prev != len(graph[a][1]):
                flag = True

            prev = len(graph[b][0])
            graph[b][0].update(graph[a][0])
            if prev != len(graph[b][0]):
                flag = True

    ans = 0

    for i in range(1, n + 1):
        if len(graph[i][0]) + len(graph[i][1]) == n - 1:
            ans += 1

    return ans
