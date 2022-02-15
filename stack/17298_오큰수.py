import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
st = []
ans = []

for i in range(n-1, -1, -1):
    if not st:
        ans.append(-1)
        st.append(li[i])
        continue
    while st:
        if li[i] < st[-1]:
            ans.append(st[-1])
            st.append(li[i])
            break
        else:
            st.pop()
    else:
        ans.append(-1)
        st.append(li[i])

print(*ans[::-1])