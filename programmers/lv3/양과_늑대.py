answer = 1
graph: list


def recur(info, idx, sheep, wolf, wolves):
    li = [idx]
    while li:
        x = li.pop()
        for y in graph[x]:
            if info[y]:
                wolves.add(y)
            else:
                sheep += 1
                li.append(y)

    global answer
    answer = max(answer, sheep)

    if sheep != wolf + 1:
        for v in wolves:
            recur(info, v, sheep, wolf + 1, wolves ^ set([v]))


def solution(info, edges):
    global graph
    graph = [[] for _ in range(len(info))]
    for a, b in edges:
        graph[a].append(b)
    recur(info, 0, 1, 0, set())

    return answer
