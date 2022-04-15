import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
m = int(input())
graph = [[float('inf') for _ in range(n)] for _ in range(n)]
pre = [[-1 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1][b - 1] = min(graph[a - 1][b - 1], c)
    pre[a - 1][b - 1] = a - 1

for i in range(n):
    graph[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                pre[i][j] = pre[k][j]

for i in range(n):
    for j in range(n):
        if i == j or graph[i][j] == float('inf'):
            print('0 ')
        else:
            print(str(graph[i][j]) + ' ')
    print('\n')

for i in range(n):
    for j in range(n):
        if pre[i][j] == -1:
            print('0\n')
            continue

        route = [j + 1]
        k = j
        while pre[i][k] != i:
            if pre[i][k] == -1:
                print('0\n')
                break
            route.append(pre[i][k] + 1)
            k = pre[i][k]
        else:
            route.append(i + 1)
            print(str(len(route)) + ' ')
            for idx in range(len(route) - 1, -1, -1):
                print(str(route[idx]) + ' ')
            print('\n')