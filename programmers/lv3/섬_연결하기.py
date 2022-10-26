parent: list


def find(x):
    if parent[x] < 0:
        return x

    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return True

    if x > y:
        x, y = y, x

    parent[x] += parent[y]
    parent[y] = x


def solution(n, costs):
    global parent
    parent = [-1] * n
    costs.sort(key=lambda x: x[2])

    answer = 0
    cnt = 0
    for a, b, c in costs:
        if union(a, b):
            continue
        answer += c
        cnt += 1

        if cnt == n - 1:
            break

    return answer
