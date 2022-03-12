from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    v, e = map(int, input().split())

    graph = {i:[] for i in range(1, v + 1)}

    for _ in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    color = {i: 0 for i in range(1, v + 1)}
    visited = set()

    flag = 1

    for i in range(1, v + 1):
        if i in visited:
            continue
        visited.add(i)
        color[i] = 1
        dq = deque([i])
        while dq:
            x = dq.popleft()

            for v in graph[x]:
                if color[v] == 0:
                    color[v] = color[x] * (-1)
                    if v not in visited:
                        dq.append(v)
                        visited.add(v)
                elif color[v] == color[x]:
                    flag = 0
                    break

            else:
                continue
            break
        else:
            continue
        break

    print('YES' if flag else 'NO')