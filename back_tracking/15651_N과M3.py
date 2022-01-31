import sys
from itertools import product
n, m = map(int, sys.stdin.readline().split())
li = list(map(str, range(1, n+1)))
print('\n'.join(map(' '.join, product(li, repeat=m))))