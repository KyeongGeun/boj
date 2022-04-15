n = int(input())

f = 1
for i in range(2, n+1):
    f *= i
f = str(f)

ans = 0
for i in range(1, len(f)+1):
    if f[-i] == '0':
        ans += 1
    else:
        break

print(ans)

# cnt = 0
# while n >= 5:
#     cnt += n // 5
#     n //= 5

# print(cnt)