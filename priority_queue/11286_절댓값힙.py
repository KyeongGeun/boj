import sys
input = sys.stdin.readline

def lessthan(a, b):
    if abs(a) < abs(b) or ( abs(a) == abs(b) and a < b):
        return 1
    else:
        return 0

def heap_push(li, v):
    li.append(v)
    item = v
    idx = len(li) - 1
    
    while idx > 0:
        parent_idx = (idx - 1) // 2
        parent = li[parent_idx]
        if lessthan(item, parent):
            li[idx] = parent
            idx = parent_idx
            continue
        break
    li[idx] = item

def heap_pop(li):
    last = li.pop()

    if li:
        return_value = li[0]
        li[0] = last

        end = len(li)
        idx = 0
        item = li[0]
        child_idx = 2 * idx + 1
        while child_idx < end:
            right_idx = child_idx + 1

            if right_idx == len(li):
                if lessthan(li[child_idx], item):
                    li[idx] = li[child_idx]
                    idx = child_idx
                break
            elif lessthan(li[child_idx], li[right_idx]):
                if lessthan(li[child_idx], item):
                    li[idx] = li[child_idx]
                    idx = child_idx
                    child_idx = idx * 2 + 1
                else:
                    break
            else:
                if lessthan(li[right_idx], item):
                    li[idx] = li[right_idx]
                    idx = right_idx
                    child_idx = idx * 2 + 1
                else:
                    break
        li[idx] = item

        return return_value

    return last

li = []
ans = []

for _ in range(int(input())):
    num = int(input())
    if num == 0:
        if li:
            ans.append(heap_pop(li))
        else:
            ans.append(0)
    else:
        heap_push(li, num)

print(*ans, sep='\n')