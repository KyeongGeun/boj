from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))

    m = int(input())
    graph = [set() for _ in range(n + 1)]
    degree = [0] * (n + 1)

    se = set()
    for _ in range(m):
        a, b = map(int, input().split())
        se.add((a, b))
        se.add((b, a))

    for i in range(n):
        for j in range(i + 1, n):
            if (li[i], li[j]) in se:
                graph[li[j]].add(li[i])
                degree[li[i]] += 1
            else:
                graph[li[i]].add(li[j])
                degree[li[j]] += 1

    dq = deque()
    for i in range(1, n + 1):
        if degree[i] == 0:
            dq.append(i)

    ans = []
    for _ in range(n):
        if not dq:
            print('IMPOSSIBLE')
            break

        if len(dq) > 1:
            print('?')
            break

        x = dq.popleft()
        ans.append(x)

        for v in graph[x]:
            degree[v] -= 1

            if degree[v] == 0:
                dq.append(v)
    else:
        print(*ans)
