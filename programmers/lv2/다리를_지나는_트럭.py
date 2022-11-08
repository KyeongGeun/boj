from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0

    truck_weights = truck_weights[::-1]
    dq = deque()
    cur = 0
    while dq or truck_weights:
        answer += 1

        if dq and dq[0][1] == answer:
            cur -= dq.popleft()[0]

        if (truck_weights and truck_weights[-1] + cur > weight) or len(dq) == bridge_length:
            continue

        if truck_weights:
            cur += truck_weights[-1]
            dq.append((truck_weights.pop(), answer + bridge_length))

    return answer
