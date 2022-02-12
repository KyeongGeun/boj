*li, = input().split('-')

s = sum(map(int, li[0].split('+')))

for i in range(1, len(li)):
    s -= sum(map(int, li[i].split('+')))

print(s)