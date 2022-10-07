def solution(m, n, puddles):
    brd = [[0] * (n + 1) for _ in range(m + 1)]

    for a, b in puddles:
        brd[a][b] = -1

    brd[0][1] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if brd[i][j] == -1:
                brd[i][j] = 0
            else:
                brd[i][j] = (brd[i - 1][j] + brd[i][j - 1]) % 1_000_000_007

    return brd[m][n]
