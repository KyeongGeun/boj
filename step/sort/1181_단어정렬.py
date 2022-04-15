import sys
input = sys.stdin.readline
set = set()
for _ in range(int(input())):
    set.add((input().rstrip()))
set = list(set)
set.sort(key=lambda a:(len(a), a))
print(*set, sep='\n')