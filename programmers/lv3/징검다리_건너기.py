def solution(stones, k):

    l, r = min(stones), max(stones)

    while l <= r:
        mid = (l + r) // 2

        cnt = 0
        for v in stones:
            if v < mid:
                cnt += 1
                if cnt == k:
                    r = mid - 1
                    break
            else:
                cnt = 0
        else:
            l = mid + 1

    return r
