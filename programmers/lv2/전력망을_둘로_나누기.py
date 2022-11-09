from collections import deque


def solution(n, wires):
    answer = n

    graph = [[] for _ in range(n + 1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    for a, b in wires:

        left = 1
        bit = (1 << a) | (1 << b)
        dq = deque([a])
        while dq:
            x = dq.popleft()

            for y in graph[x]:
                if bit & (1 << y):
                    continue
                bit |= (1 << y)
                left += 1
                dq.append(y)

        right = 1
        bit = (1 << a) | (1 << b)
        dq = deque([b])
        while dq:
            x = dq.popleft()

            for y in graph[x]:
                if bit & (1 << y):
                    continue
                bit |= (1 << y)
                right += 1
                dq.append(y)

        answer = min(answer, abs(left - right))

    return answer
