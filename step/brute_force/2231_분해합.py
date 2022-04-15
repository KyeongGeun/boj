n = int(input())
a = 0
for i in range(0 if n <= 18 else n-len(str(n))*9, n):
    s = i + sum(map(int, list(str(i))))
    if s == n:
        a = i
        break 
print(a)