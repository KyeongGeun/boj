def solution(progresses, speeds):
    answer = []

    prev = -1
    cnt = 0
    for a, b in zip(progresses, speeds):
        c = (100 - a - 1) // b + 1
        if prev >= c:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            prev = c

    answer.append(cnt)

    return answer[1:]
