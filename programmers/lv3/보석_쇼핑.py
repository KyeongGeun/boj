def solution(gems):
    answer = []
    total = len(set(gems))

    dic = {}
    l, r = 0, 0

    minv = float('inf')

    while r < len(gems):
        dic.setdefault(gems[r], 0)
        dic[gems[r]] += 1

        while gems[l] in dic and dic[gems[l]] > 1:
            dic[gems[l]] -= 1
            l += 1

        if len(dic) == total and minv > r - l:
            minv = r - l
            answer = [l + 1, r + 1]

        r += 1

    return answer
