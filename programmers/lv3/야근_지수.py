def solution(n, works):
    answer = 0

    works.sort(reverse=True)

    while n > 0 and works[0] != 0:
        temp = works[0]
        for i in range(len(works)):
            if works[i] != temp:
                break
            works[i] -= 1
            n -= 1
            if n == 0:
                break

    for v in works:
        answer += v * v

    return answer
