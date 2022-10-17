def solution(s):
    answer = []

    for c in s:
        li = []
        l = 0
        llo = 0
        for x in c:
            if x == '1':
                l += 1
            elif l > 1:
                l -= 2
                llo += 1
            else:
                if l:
                    li.append('1' * l)
                    l = 0
                li.append('0')

        if llo:
            li.append('110' * llo)
        if l:
            li.append('1' * l)

        answer.append(''.join(li))

    return answer
