from collections import deque


def solution(begin, target, words):
    l = len(words[0])
    graph = {}
    words.append(begin)

    for v in words:
        graph[v] = []

    for i in range(len(words)):
        for j in range(len(words)):
            if i == j:
                continue

            cnt = 0
            for k in range(l):
                if words[i][k] != words[j][k]:
                    cnt += 1

            if cnt == 1:
                graph[words[i]].append(words[j])
                graph[words[j]].append(words[i])

    dq = deque()
    dq.append(begin)

    visited = set()
    visited.add(begin)

    answer = 0
    while dq:
        answer += 1
        for _ in range(len(dq)):
            x = dq.popleft()

            for v in graph[x]:
                if v in visited:
                    continue
                visited.add(v)

                if v == target:
                    return answer

                dq.append(v)

    return 0
