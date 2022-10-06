def solution(n, s):
    if s // n == 0:
        return [-1]

    return [s // n] * (n - s % n) + ([s // n + 1] * (s % n))
