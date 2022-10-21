def solution(a):
    if len(a) < 2:
        return 0

    cnt = [0] * len(a)
    memo = [-1] * len(a)

    if a[0] != a[1]:
        cnt[a[0]] += 1
        memo[a[0]] = 1

    for i in range(1, len(a) - 1):
        l, x, r = a[i - 1], a[i], a[i + 1]

        if l != x and memo[x] != i - 1:
            cnt[x] += 1
        elif x != r:
            cnt[x] += 1
            memo[x] = i + 1

    if a[-1] != a[-2] and memo[a[-1]] != len(a) - 2:
        cnt[a[-1]] += 1

    return max(cnt) << 1
