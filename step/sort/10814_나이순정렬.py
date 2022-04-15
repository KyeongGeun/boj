import sys
input()
s = sys.stdin.readlines()
s.sort(key=lambda x:int(x.split()[0]))
print(''.join(s), end='')