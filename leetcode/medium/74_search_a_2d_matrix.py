class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        l, r = 0, m - 1

        while l <= r:
            mid = (l + r) // 2
            print(mid)
            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][-1] < target:
                l = mid + 1
            else:
                break

        i = mid

        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[i][mid] > target:
                r = mid - 1
            elif matrix[i][mid] < target:
                l = mid + 1
            else:
                return True

        return False
