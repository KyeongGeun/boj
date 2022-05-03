def getPi(str):
    m = len(str)
    j = 0
    pi = [0] * (m)
    for i in range(1, m):
        while j > 0 and str[i] != str[j]:
            j = pi[j - 1]

        if str[i] == str[j]:
            j += 1
            pi[i] = j

    return pi


def kmp(str1, str2):
    n = len(str1)
    m = len(str2)
    pi = getPi(str2)
    j = 0
    ret = []
    for i in range(n):
        while j > 0 and str1[i] != str2[j]:
            j = pi[j - 1]

        if str1[i] == str2[j]:
            if j == m - 1:
                ret.append(i - m + 2)
                j = pi[j]

            else:
                j += 1

    return ret


str1 = input()
str2 = input()

li = kmp(str1, str2)
print(len(li))
print(*li)
