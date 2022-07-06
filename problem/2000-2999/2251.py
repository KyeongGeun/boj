from collections import deque

*_max, = map(int, input().split())

already = [[[False for _ in range(_max[2] + 1)]
            for _ in range(_max[1] + 1)] for _ in range(_max[0] + 1)]

already[0][0][_max[2]] = True

ans = []

dq = deque()
dq.append([0, 0, _max[2]])

_set = set([_max[2]])
while dq:
    li = dq.popleft()

    for i in range(3):
        for j in range(2):
            target = (i + j + 1) % 3

            new = li[:]
            if li[i] + li[target] >= _max[target]:
                new[i] = li[i] + li[target] - _max[target]
                new[target] = _max[target]
            else:
                new[i] = 0
                new[target] = li[i] + li[target]

            if already[new[0]][new[1]][new[2]]:
                continue

            already[new[0]][new[1]][new[2]] = True

            if new[0] == 0:
                _set.add(new[2])

            dq.append(new)

print(*sorted(_set))
