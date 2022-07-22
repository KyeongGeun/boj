import sys
input = sys.stdin.readline


def belman():
    min_d = [2000000000] * (n + 1)
    min_d[1] = 0

    for i in range(n):
        for j in range(len(graph)):
            a, b, c = graph[j]

            d = min_d[a] + c

            if min_d[b] > d:
                min_d[b] = d

                if i == n - 1:
                    return True

    return False


ans = []
for _ in range(int(input())):
    n, m, w = map(int, input().split())

    graph = []

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph.append((a, b, c))
        graph.append((b, a, c))

    for _ in range(w):
        a, b, c = map(int, input().split())
        graph.append((a, b, -c))

    if belman():
        ans.append('YES')
    else:
        ans.append('NO')

print(*ans, sep='\n')
