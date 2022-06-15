import sys
input = sys.stdin.readline


def generate(x, lis, num, etc):
    if x == l:
        for v in lis:
            if v in aeiou:
                if num + 1 < 1 or etc < 2:
                    continue
            else:
                if num < 1 or etc + 1 < 2:
                    continue
            yield v

    else:
        for i in range(len(lis)):
            if lis[i] in aeiou:
                for v in generate(x + 1, lis[i + 1:], num + 1, etc):
                    yield lis[i] + v
            else:
                for v in generate(x + 1, lis[i + 1:], num, etc + 1):
                    yield lis[i] + v


l, c = map(int, input().split())

li = input().split()
li.sort(key=lambda x: ord(x))

aeiou = set(['a', 'e', 'i', 'o', 'u'])

print(*list(generate(1, li, 0, 0)), sep='\n')
