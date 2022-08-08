import re
import sys
input = sys.stdin.readline

n = int(input())
ans = []
for i in range(n):
    s = input().rstrip()
    if re.match("^((100+1+)|(01))+$", s):
        ans.append('YES')
    else:
        ans.append('NO')

print('\n'.join(ans))
