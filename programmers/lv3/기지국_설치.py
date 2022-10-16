def solution(n, stations, w):
    l, r = 0, 0
    leng = 2 * w + 1
    answer = 0
    for x in stations:
        nl, nr = x - w, x + w

        if nl <= r + 1:
            r = nr
        else:
            answer += (nl - r - 2) // leng + 1
            l, r = nl, nr

    if r < n:
        answer += (n - r - 1) // leng + 1

    return answer
