from collections import deque


def bfs(n, computers, i, visited):
    dq = deque([i])
    visited[i] = True

    while dq:
        x = dq.popleft()

        for j in range(n):
            if not visited[j] and computers[x][j]:
                visited[j] = True
                dq.append(j)


def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        if visited[i]:
            continue
        bfs(n, computers, i, visited)
        answer += 1

    return answer
