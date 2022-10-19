from collections import deque


def solution(N, number):
    dp = [float('inf')] * 1_000_001
    dq = deque()
    se = set()

    temp = 0
    for i in range(5):
        temp += N * (10 ** i)
        dp[temp] = i + 1
        dq.append(temp)
        se.add(temp)

    while dq:
        x = dq.popleft()

        temp = set()
        for y in se:
            if dp[x] + dp[y] > 8:
                continue
            for v in (x // y, y // x, abs(x - y), x + y, x * y):
                if v < 1 or v > len(dp) - 1:
                    continue

                next = dp[x] + dp[y]

                if dp[v] <= next:
                    continue
                dp[v] = next

                dq.append(v)
                temp.add(v)

        se.update(temp)

    return -1 if dp[number] > 8 else dp[number]
