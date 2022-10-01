def solution(routes):
    ans = 1
    routes.sort()

    r = routes[0][1]

    for a, b in routes:
        if r < a:
            ans += 1
            r = b
        else:
            r = min(r, b)

    return ans
