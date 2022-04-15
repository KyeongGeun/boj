n, k = map(int, input().split())

def foo(n, k, b):
    return bar(n, b)-bar(n-k, b)-bar(k, b)
    
def bar(a, b):
    cnt = 0
    while a >= b:
        cnt += a//b
        a //= b
    return cnt

print(min(foo(n, k, 5), foo(n, k, 2)))