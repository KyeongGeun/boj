def solution(enroll, referral, seller, amount):

    dic = {}
    dic['-'] = [0, None]
    for name, parent in zip(enroll, referral):
        dic[name] = [0, dic[parent]]

    for name, number in zip(seller, amount):
        next = dic[name]
        number *= 100
        while next and number:
            temp = number // 10
            next[0] += number - temp
            number = temp
            next = next[1]

    return [dic[k][0] for k in enroll]
