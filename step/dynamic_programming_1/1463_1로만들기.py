n = int(input()) # 1 ~ 1,000,000

li = [0]*(n+1)

for i in range(2, n+1):
    if i % 3 == 0 and i % 2 == 0:
        li[i] = min(li[i//3] + 1, li[i//2] + 1, li[i-1] + 1)
    elif i % 3 == 0:
        li[i] = min(li[i//3] + 1, li[i-1] + 1)
    elif i % 2 == 0:
        li[i] = min(li[i//2] + 1, li[i-1] + 1)
    else:
        li[i] = li[i-1] + 1

print(li[n])