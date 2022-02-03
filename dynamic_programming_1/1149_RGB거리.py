import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

sum = []
n = int(input())
cost = [[v for v in map(int, input().split())] for _ in range(n)]
memo = {}
def foo(I, J):
    if I == 0:
        return cost[I][J]
    elif J == 0:
        if (I-1, 1) not in memo.keys():
            memo[I-1, 1] = foo(I-1, 1)
        if (I-1, 2) not in memo.keys():
                memo[I-1, 2] = foo(I-1, 2)
        return cost[I][J] + min(memo[I-1, 1], memo[I-1, 2])
    elif J == 1:
        if (I-1, 0) not in memo.keys():
            memo[I-1, 0] = foo(I-1, 0)
        if (I-1, 2) not in memo.keys():
                memo[I-1, 2] = foo(I-1, 2)
        return cost[I][J] + min(memo[I-1, 0], memo[I-1, 2])
    else:
        if (I-1, 0) not in memo.keys():
            memo[I-1, 0] = foo(I-1, 0)
        if (I-1, 1) not in memo.keys():
                memo[I-1, 1] = foo(I-1, 1)
        return cost[I][J] + min(memo[I-1, 0], memo[I-1, 1])
    
print(min(foo(n-1,0), foo(n-1,1), foo(n-1,2)))