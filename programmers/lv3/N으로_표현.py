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


def solution2(N, number):
    if number == N:
        return 1

    dp = [0] * 9

    for i in range(1, 9):
        dp[i] = [int(str(N) * i)]

    for i in range(2, 9):
        for j in range(1, i // 2 + 1):
            for k in dp[i - j]:
                for l in dp[j]:
                    s = set()
                    s.add(k + l)
                    s.add(abs(k - l))
                    s.add(k * l)
                    if l != 0:
                        s.add(k // l)
                    if k != 0:
                        s.add(l // k)
                    dp[i] = list(set(dp[i]) | s)
        if number in dp[i]:
            return i

    return -1
