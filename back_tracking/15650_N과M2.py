import sys
from itertools import combinations
n, m = map(int, sys.stdin.readline().split())
li = map(str, range(1, n+1))
print('\n'.join(map(' '.join, combinations(li, m))))