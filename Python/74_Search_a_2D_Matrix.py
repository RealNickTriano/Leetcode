from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """

        """
        l, r = 0, len(matrix) - 1

        while l <= r:
            m = (r + l) // 2
            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
            else:
                break

        if not (l <= r):
            return False

        m = (r + l) // 2
        l, r = 0, len(matrix[0]) - 1

        while l <= r:
            m2 = (r + l) // 2
            if target > matrix[m][m2]:
                l = m2 + 1
            elif target < matrix[m][m2]:
                r = m2 - 1
            else:
                return True

        return False


sol = Solution()
print(sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
