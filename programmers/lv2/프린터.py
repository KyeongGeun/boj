from collections import deque


def solution(priorities, location):
    cnt = [0] * 10
    for v in priorities:
        cnt[v] += 1

    answer = 0
    dq = deque(priorities)
    for i in range(9, 0, -1):
        while cnt[i] > 0:
            if dq[0] == i:
                answer += 1
                if location == 0:
                    return answer
                dq.popleft()
                cnt[i] -= 1
            else:
                dq.append(dq.popleft())
            location = (location - 1) % len(dq)

    return answer
