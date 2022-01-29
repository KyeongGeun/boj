import sys

input = sys.stdin.readline
n = int(input())
arr = []
cnt = [0]*8001

for i in range(n):
    cnt[int(input())] += 1
for i in range(-4000, 4001):
    for j in range(cnt[i]):
        arr.append(i)

li = list(filter(lambda i:cnt[i] == max(cnt), range(-4000, 4001)))

print(round(sum(arr)/n))
print(arr[n//2])
print(li[0] if len(li)<2 else li[1])
print(max(arr)-min(arr))