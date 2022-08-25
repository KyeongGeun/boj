import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    li = list(map(int, input().split()))

    for j in range(1, len(li)):
        if li[j] < i:
            continue
        graph[i].append(li[j])
        graph[li[j]].append(i)

team = [[] for _ in range(2)]

visited = [False for _ in range(n + 1)]
stack = []

for i in range(1, n + 1):
    if visited[i]:
        continue
    visited[i] = True
    team[0].append(i)

    stack.append((i, 0))

    while stack:
        x, t = stack.pop()
        newT = (t + 1) % 2

        for v in graph[x]:
            if visited[v]:
                continue
            visited[v] = True
            team[newT].append(v)
            stack.append((v, newT))

print(len(team[0]))
print(*sorted(team[0]))
print(len(team[1]))
print(*sorted(team[1]))
