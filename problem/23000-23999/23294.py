from collections import deque

n, q, c = map(int, input().split())

cap = [0] + list(map(int, input().split()))

cur = -1
prev = deque()
next = deque()

cache = 0

for _ in range(q):
    li = input().split()

    if li[0] == 'B':
        if not prev:
            continue
        next.append(cur)
        cur = prev.pop()

    elif li[0] == 'F':
        if not next:
            continue
        prev.append(cur)
        cur = next.pop()

    elif li[0] == 'A':
        for v in next:
            cache -= cap[v]
        next.clear()

        a = int(li[1])
        cache += cap[a]

        if cur != -1:
            prev.append(cur)
        cur = a

        while cache > c:
            cache -= cap[prev.popleft()]

    else:
        if not prev:
            continue

        newPrev = deque()
        for i in range(len(prev) - 1):
            if prev[i] == prev[i + 1]:
                cache -= cap[prev[i]]
                continue
            newPrev.append(prev[i])
        newPrev.append(prev[-1])

        prev = newPrev


print(cur)
if prev:
    print(*list(prev)[::-1])
else:
    print(-1)

if next:
    print(*list(next)[::-1])
else:
    print(-1)
