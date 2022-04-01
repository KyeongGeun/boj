import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
graph = [[] for _ in range(n)]
pre = [-1] * n
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

stack = [0]
while stack:
    x = stack.pop()
    for v in graph[x]:
        if pre[v] == -1:
            pre[v] = x + 1
            stack.append(v)

for i in range(1, len(pre)):
    print(str(pre[i]) + '\n')