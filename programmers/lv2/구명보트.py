def solution(people, limit):
    two = 0

    people.sort()

    l, r = 0, len(people) - 1

    while l < r:
        if people[l] + people[r] <= limit:
            l += 1
            two += 1
        r -= 1

    return len(people) - two
