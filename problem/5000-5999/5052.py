import sys
input = sys.stdin.readline

ans = []
for _ in range(int(input())):
    d = {}

    flag = False

    for _ in range(int(input())):
        s = input().rstrip()
        if flag:
            continue

        temp = d
        for i in range(len(s) - 1):
            c = s[i]
            if c in temp:
                if temp[c] == -1:
                    flag = True
                    break
            else:
                temp[c] = {}
            temp = temp[c]

        if s[-1] in temp:
            flag = True
        else:
            temp[s[-1]] = -1

    if flag:
        ans.append('NO')
    else:
        ans.append('YES')

print(*ans, sep='\n')
