def solution(s):
    answer = 1

    for i in range(len(s)):
        temp = 1
        for j in range(1, min(i + 1, len(s) - i)):
            if s[i - j] == s[i + j]:
                temp += 2
            else:
                break
        answer = max(answer, temp)

    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            continue
        temp = 2
        for j in range(1, min(i + 1, len(s) - i - 1)):
            if s[i - j] == s[i + 1 + j]:
                temp += 2
            else:
                break
        answer = max(answer, temp)

    return answer
