answer = -1


def recur(cur, word):
    global answer
    answer += 1

    if cur == word:
        return True

    if len(cur) == 5:
        return False

    for c in ('A', 'E', 'I', 'O', 'U'):
        if recur(cur + c, word):
            return True

    return False


def solution(word):
    recur('', word)
    return answer
