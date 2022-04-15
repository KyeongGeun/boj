import sys
input = sys.stdin.readline
dict = {}

for _ in range(int(input())):
    for _ in range(int(input())):
        a, b = input().split()
        if b in dict.keys():
            dict[b] += 1
        else:
            dict[b] = 1
    ans = 1
    for i, v in dict.items():
        ans *= v+1
    print(ans - 1)
    dict = {}