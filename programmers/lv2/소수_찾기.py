sset = set()


def recur(s, cur, bit):
    if len(cur) == len(s):
        return

    for i in range(len(s)):
        if bit & (1 << i):
            continue

        new = cur + s[i]
        sset.add(int(new))
        recur(s, new, bit | (1 << i))


def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if not n % 2:
        return False

    for i in range(3, int(n ** .5) + 1):
        if not n % i:
            return False

    return True


def solution(numbers):
    recur(numbers, '', 0)

    answer = 0
    for v in sset:
        if isPrime(v):
            answer += 1

    return answer
