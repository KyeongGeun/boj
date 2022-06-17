n = int(input())


def star(x):
    if x == 1:
        return ['*']

    li = star(x - 1)

    new_li = []
    if x % 2:  # 홀수
        l = len(li)
        o, i = l * 2 - 1, 1

        new_li.append(' ' * (o + 1) + '*' + ' ' * (o + 1))

        for _ in range(l - 1):
            new_li.append(' ' * o + '*' + ' ' * i + '*' + ' ' * o)
            o -= 1
            i += 2

        for v in li:
            new_li.append(' ' * o + '*' + ' ' * ((i - len(v)) // 2) +
                          v + ' ' * ((i - len(v)) // 2) + '*' + ' ' * o)
            o -= 1
            i += 2

        new_li.append('*' * (i + 2))
        return new_li
    else:
        o, i = 1, len(li) * 4 - 3

        new_li.append('*' * (i + 4))

        for v in li:
            new_li.append(' ' * o + '*' + ' ' * ((i - len(v)) // 2) +
                          v + ' ' * ((i - len(v)) // 2) + '*' + ' ' * o)
            o += 1
            i -= 2
        for _ in range(len(li) - 1):
            new_li.append(' ' * o + '*' + ' ' * i + '*' + ' ' * o)
            o += 1
            i -= 2

        new_li.append(' ' * (o) + '*' + ' ' * (o))
        return new_li


for v in star(n):
    print(v.rstrip())
