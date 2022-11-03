def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)

    l, r = 0, distance

    while l <= r:
        mid = (l + r) // 2

        cnt = 0
        prev = 0
        for v in rocks:
            if v - prev < mid:
                cnt += 1
                if cnt > n:
                    r = mid - 1
                    break
            else:
                prev = v
        else:
            l = mid + 1

    return r
