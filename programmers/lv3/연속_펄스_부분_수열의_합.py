def solution(sequence):
    acc = [0] * len(sequence)
    acc[0] = sequence[0]

    for i in range(1, len(sequence)):
        acc[i] = acc[i - 1] + sequence[i] * (-1) ** (i % 2)

    maxv = max(acc)
    minv = min(acc)

    return max(maxv, abs(minv), maxv - minv)
