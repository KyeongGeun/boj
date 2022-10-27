def solution(a):
    answer = 2

    if len(a) <= 2:
        return len(a)

    leftMin = [a[0]]
    rightMin = [0] * len(a)
    rightMin[-1] = a[-1]
    for i in range(1, len(a)):
        if a[i] < leftMin[-1]:
            leftMin.append(a[i])
        else:
            leftMin.append(leftMin[-1])

        if a[-i - 1] < rightMin[-i]:
            rightMin[-i - 1] = a[-i - 1]
        else:
            rightMin[-i - 1] = rightMin[-i]

    for i in range(1, len(a) - 1):
        if leftMin[i - 1] > a[i] or rightMin[i + 1] > a[i]:
            answer += 1

    return answer
