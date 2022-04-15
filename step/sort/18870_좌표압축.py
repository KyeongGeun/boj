import sys
n = int(sys.stdin.readline())
*arr, = map(int, sys.stdin.readline().split())
li = list(set(arr))
li.sort()
dict = {}
for i in range(len(li)):
    dict[li[i]] = i
for i in range(len(arr)):
    arr[i] = dict[arr[i]]
sys.stdout.write(' '.join(map(str, arr)))