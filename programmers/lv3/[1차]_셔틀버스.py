def strToTime(s):
    a, b = s.split(':')
    return int(a) * 60 + int(b)


def timeToStr(t):
    return f'{t // 60:02}' + ':' + f'{t % 60:02}'


def solution(n, t, m, timetable):
    answer = ''
    times = sorted([strToTime(v) for v in timetable], reverse=True)

    for busTime in range(540, 540 + (n - 1) * t + 1, t):
        cnt = 0
        while times and times[-1] <= busTime:
            cnt += 1
            if cnt == m:
                answer = timeToStr(times.pop() - 1)
                break
            times.pop()
        else:
            answer = timeToStr(busTime)

    return answer
