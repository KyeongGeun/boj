import sys
from itertools import combinations_with_replacement as co
n, m = map(int, sys.stdin.readline().split())
li = list(map(str, range(1, n+1)))
print('\n'.join(map(' '.join, co(li, m))))