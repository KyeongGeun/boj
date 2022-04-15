import sys
input = sys.stdin.readline

dict = {}
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        if (20, 20, 20) not in dict.keys():
            dict[20, 20, 20] = w(20, 20, 20)
        return dict[20,20,20]
    elif (a, b, c) in dict.keys():
        return dict[a, b, c]
    elif a < b < c:
        if (a, b, c-1) not in dict.keys():
            dict[a, b, c-1] = w(a, b, c-1)
        if (a, b-1, c-1) not in dict.keys():
            dict[a, b-1, c-1] = w(a, b-1, c-1)
        if (a, b-1, c) not in dict.keys():
            dict[a, b-1, c] = w(a, b-1, c)
        return dict[a, b, c-1] + dict[a, b-1, c-1] - dict[a, b-1, c]
    
    if (a-1, b, c) not in dict.keys():
        dict[a-1, b, c] = w(a-1, b, c)
    if (a-1, b-1, c) not in dict.keys():
        dict[a-1, b-1, c] = w(a-1, b-1, c)
    if (a-1, b, c-1) not in dict.keys():
        dict[a-1, b, c-1] = w(a-1, b, c-1)
    if (a-1, b-1, c-1) not in dict.keys():
        dict[a-1, b-1, c-1] = w(a-1, b-1, c-1)
    return dict[a-1, b, c] + dict[a-1, b-1, c] + dict[a-1, b, c-1] - dict[a-1, b-1, c-1]

while 1:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    sys.stdout.write(f'w({a}, {b}, {c}) = ' + str(w(a,b,c)) + '\n')