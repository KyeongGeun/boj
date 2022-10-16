from heapq import heappush, heappop


def solution(n, paths, gates, summits):
    answer = [1, 10_000_001]

    graph = [[] for _ in range(n + 1)]

    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))

    gateSet = set(gates)
    summitSet = set(summits)
    for i in sorted(summits):
        hq = [(0, i)]
        min_d = [10_000_001] * (n + 1)
        min_d[i] = 0

        while hq:
            d, x = heappop(hq)

            if min_d[x] < d:
                continue

            for y, w in graph[x]:
                if y in summitSet:
                    continue
                new_d = max(d, w)
                if y in gateSet:
                    if answer[1] > new_d:
                        answer = [i, new_d]
                    if new_d == d:
                        break
                    continue

                if min_d[y] > new_d:
                    min_d[y] = new_d
                    heappush(hq, (new_d, y))
            else:
                continue
            break

    return answer
