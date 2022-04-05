import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

li = []
while True:
    try:
        li.append(int(input()))
    except:
        break

def pre(start, end):
    if start > end - 1:
        return
        
    idx = end
    for i in range(start + 1, end):
        if li[start] < li[i]:
            idx = i
            break
    
    pre(start + 1, idx)
    pre(idx, end)
    print(li[start])

pre(0, len(li))