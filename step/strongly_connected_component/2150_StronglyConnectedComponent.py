import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
print = sys.stdout.write

v, e = map(int, input().split())

graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)

stack = []
visited = [False] * (v + 1)
finished = [False] * (v + 1)
idx = [0] * (v + 1)
cnt = 0


def func(n):
    global cnt
    cnt += 1
    idx[n] = cnt
    visited[n] = True
    stack.append(n)
    value = cnt

    for v in graph[n]:
        if not visited[v]:
            value = min(value, func(v))
        elif not finished[v]:
            value = min(value, idx[v])
    
    if value == idx[n]:
        li = []
        while stack:
            x = stack.pop()
            li.append(x)
            finished[x] = True

            if n == x:
                li.sort()
                li.append(-1)
                ans.append(li)
                break

    return value


ans = []

for i in range(1, v + 1):
    if not visited[i]:
        func(i)


ans.sort()
print(str(len(ans)) + '\n')
for l in ans:
    for v in l:
        print(str(v) + ' ')
    print('\n')
    
