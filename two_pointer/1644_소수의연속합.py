n = int(input())

prime = [False, False] + [True] * (n - 1)

for i in range(2, int(n ** .5) + 1):
    if prime[i]:
        for j in range(i * 2, n + 1, i):
            prime[j] = False

accum = [0, 2]

for i in range(3, n + 1):
    if prime[i]:
        accum.append(accum[-1] + i)

i, j = 0, 1
cnt = 0

while i < j < len(accum):
    num = accum[j] - accum[i]
    if num > n:
        i += 1
    elif num < n:
        j += 1
    else:
        cnt += 1
        i += 1

print(cnt)