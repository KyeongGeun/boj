def isPrime(x):
    for i in range(2, int(x ** .5) + 1):
        if x % i == 0:
            return False
    return True


def recur(cnt, num):
    if cnt == n:
        ans.append(num)
        return

    for i in odd:
        newNum = num * 10 + i

        if isPrime(newNum):
            recur(cnt + 1, newNum)


n = int(input())

odd = (1, 3, 7, 9)

ans = []

for i in (2, 3, 5, 7):
    recur(1, i)

print(*ans, sep='\n')
