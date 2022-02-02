import sys
from itertools import combinations
input = sys.stdin.readline
n = int(input())
stat = []
li = [[*map(int, input().split())] for _ in range(n)]

def calcu(one):
    for i in range(len(one)//2):
        o = one[i]
        t = [n for n in range(n) if n not in o]
        s = [0, 0]
        for i in range(len(o)):
            for j in range(i+1, len(o)):
                s[0] += li[o[i]][o[j]] + li[o[j]][o[i]]
        for i in range(len(t)):
            for j in range(i+1, len(t)):
                s[1] += li[t[i]][t[j]] + li[t[j]][t[i]]
        if s[0]-s[1] == 0:
            print(0)
            exit(0)
        stat.append(abs(s[0]-s[1]))
calcu(combinations(range(n), n//2))
print(min(stat))