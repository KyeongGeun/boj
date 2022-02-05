n = int(input()) # 1 ~ 100

li = [[0]*10 for _ in range(n+1)]

li[1] = [0] + [1]*9

def foo(N, K):
    if N == 1: return li[N][K]

    if li[N][K] == 0:
        if K == 0:
            li[N][K] = foo(N-1, K+1) % 1000000000
        elif K == 9:
            li[N][K] = foo(N-1, K-1) % 1000000000
        else:
            li[N][K] = (foo(N-1, K-1) + foo(N-1, K+1)) % 1000000000

    return li[N][K]

print(sum(foo(n, i) for i in range(10)) % 1000000000)