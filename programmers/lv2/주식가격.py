def solution(prices):
    answer = [0] * len(prices)

    stack = []
    for i, v in enumerate(prices):
        while stack and stack[-1][1] > v:
            idx, value = stack.pop()
            answer[idx] = i - idx

        stack.append((i, v))

    while stack:
        idx, value = stack.pop()
        answer[idx] = i - idx

    return answer
