class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        setX = set()
        setY = set()
        for i in range(len(matrix)):
            for j in range((len(matrix[0]))):
                if matrix[i][j] == 0:
                    setX.add(i)
                    setY.add(j)

        for i in setX:
            for j in range(len(matrix[i])):
                matrix[i][j] = 0

        for j in setY:
            for i in range(len(matrix)):
                matrix[i][j] = 0
