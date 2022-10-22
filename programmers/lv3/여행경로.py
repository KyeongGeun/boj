answer = ['ICN']
se = set()
graph = {}


def recur(s, l):
    if len(se) == l:
        return True

    for i in range(len(graph[s])):
        e = graph[s][i]
        if (s, i) in se:
            continue

        se.add((s, i))
        answer.append(e)

        if recur(e, l):
            return True

        if (s, i) in se:
            se.remove((s, i))
        answer.pop()


def solution(tickets):
    for a, b in tickets:
        graph.setdefault(a, [])
        graph.setdefault(b, [])
        graph[a].append(b)

    for k in graph:
        graph[k].sort()

    recur('ICN', len(tickets))

    return answer
