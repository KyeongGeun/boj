import bisect
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, c = map(int, input().split())
li = list(map(int, input().split()))

def func(lis, idx):
    if idx == len(lis):
        yield 0
    else:
        for v in func(lis, idx + 1):
            yield v + lis[idx] 
            yield v

li1 = li[:n // 2]
li2 = li[n // 2:]

sum_li1 = list(func(li1, 0))
sum_li2 = list(func(li2, 0))

sum_li2.sort()

cnt = 0
for v in sum_li1:
    if c < v:
        continue
    cnt += bisect.bisect_right(sum_li2, c - v)

print(cnt)