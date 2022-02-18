import sys
input = sys.stdin.readline

def divide(a, b, c):
    
    if b == 1:
        return a%c

    result = divide(a, b//2, c)

    result *= result
    result %= c

    if b%2 != 0:
        result *= a
        result %= c

    return result

a, b, c = map(int, input().split())
print(divide(a, b, c))