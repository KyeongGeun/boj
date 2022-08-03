import sys
input = sys.stdin.readline


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
destroy = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

input()

for v in map(int, input().split()):
    destroy[v] = True

check = [False] * (n + 1)

ans = []
for i in range(1, n + 1):
    if not destroy[i]:
        continue

    for v in graph[i]:
        if not destroy[v]:
            break
    else:
        for v in graph[i]:
            check[v] = True

        check[i] = True
        ans.append(i)

for i in range(1, n + 1):
    if not destroy[i]:
        continue
    if not check[i]:
        print(-1)
        break
else:
    print(len(ans))
    print(*ans)
