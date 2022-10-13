def solution(A, B):
    answer = 0

    A.sort()
    B.sort()

    i = 0

    for a in A:
        while i < len(B) and B[i] <= a:
            i += 1
        if i == len(B):
            break
        i += 1
        answer += 1

    return answer
