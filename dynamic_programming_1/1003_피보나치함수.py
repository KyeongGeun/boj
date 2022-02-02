import sys
input = sys.stdin.readline

dict = {}
def fibonacci(n):
    global zero, one
    if (n == 0):
        return (1, 0)
    elif (n == 1):
        return (0, 1)
    else:
        if n-1 in dict.keys():
            a = dict[n-1]
        else: 
            a = dict[n-1] = fibonacci(n-1)
        if n-2 in dict.keys():
            b = dict[n-2]
        else:
            b = dict[n-2] = fibonacci(n-2)
        return tuple(i+j for i, j in zip(a, b))

n = int(input())

for _ in range(n):
    N = int(input())
    print(*fibonacci(N))