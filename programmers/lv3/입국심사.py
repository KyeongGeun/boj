def solution(n, times):
    l, r = 1, 1_000_000_000 ** 2

    while l < r:
        mid = (l + r) // 2

        cnt = 0
        for v in times:
            cnt += mid // v

        if cnt < n:
            l = mid + 1
        else:
            r = mid

    return l
