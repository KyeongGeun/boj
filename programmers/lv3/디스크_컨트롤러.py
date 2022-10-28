from heapq import heappush, heappop


def solution(jobs):
    answer = 0
    l = len(jobs)
    jobs.sort(reverse=True)

    hq = []

    cur = jobs[-1][0]
    while jobs:
        while jobs and jobs[-1][0] <= cur:
            heappush(hq, (jobs[-1][1], jobs[-1][0]))
            jobs.pop()
        if not hq:
            cur = jobs[-1][0]
        else:
            a, b = heappop(hq)
            cur += a
            answer += cur - b

    while hq:
        a, b = heappop(hq)
        cur += a
        answer += cur - b

    return answer // l
