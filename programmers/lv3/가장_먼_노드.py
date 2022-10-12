from collections import deque


def solution(n, edge):
    answer = 0

    graph = [[] for i in range(n + 1)]
    memo = [-1] * (n + 1)

    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    memo[1] = 0

    dq = deque([1])
    mmax = 0
    while dq:
        x = dq.popleft()

        for y in graph[x]:
            if memo[y] == -1:
                memo[y] = memo[x] + 1
                mmax = max(mmax, memo[y])
                dq.append(y)

    for i in range(1, n + 1):
        if memo[i] == mmax:
            answer += 1

    return answer
