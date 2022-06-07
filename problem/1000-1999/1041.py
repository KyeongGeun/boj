import sys
input = sys.stdin.readline

n = int(input())

li = list(map(int, input().split()))

graph = [5, 4, 3, 2, 1, 0]

if n == 1:
    _max = max(li)
    print(sum(li) - _max)
    exit(0)

_min = min(li)

_min2 = float('inf')
for i in range(6):
    for j in range(6):
        if i == j:
            continue
        if graph[i] == j:
            continue
        _min2 = min(_min2, li[i] + li[j])

_min3 = float('inf')
for i in range(6):
    for j in range(6):
        if i == j:
            continue
        if graph[i] == j:
            continue
        for k in range(6):
            if i == k or j == k:
                continue
            if graph[i] == k or graph[j] == k:
                continue
            _min3 = min(_min3, li[i] + li[j] + li[k])

ans = 0
ans += 4 * (n - 2) * (n - 1) * _min + (n - 2) ** 2 * _min
ans += 4 * ((n - 1) + (n - 2)) * _min2
ans += 4 * _min3

print(ans)
