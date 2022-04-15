import sys
n = int(input())
if n == 1: print('666')
else:
    num = 1666
    cnt = 2
    while 1:
        if (num+400000)%1000000 == 66_666: # num = 666666, 1666666, 2666666 일때
            num -= 666
            for i in range(1000):
                if n == cnt:
                    print(num)
                    sys.exit()
                num += 1
                cnt += 1
            num += 666
            continue
        elif (num+40000)%100000 == 6_666: # num = 66666, 166666, 266666 일때
            num -= 66
            for i in range(100):
                if n == cnt:
                    print(num)
                    sys.exit()
                num += 1
                cnt += 1
            num += 966
            continue
        elif (num+4000)%10000 == 666: # num = 6666, 16666, 26666 일때
            num -= 6
            for i in range(10):
                if n == cnt:
                    print(num)
                    sys.exit()
                num += 1
                cnt += 1
            num += 996
            continue
        elif n == cnt:
            print(num)
            sys.exit()
        num += 1000
        cnt += 1