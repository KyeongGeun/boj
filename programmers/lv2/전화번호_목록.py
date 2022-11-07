def solution(phone_book):
    sset = set()

    for s in sorted(phone_book, key=lambda x: -len(x)):
        if s in sset:
            return False
        for i in range(1, len(s) + 1):
            sset.add(s[:i])

    return True
