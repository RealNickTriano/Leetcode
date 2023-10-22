from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # O(n)

        l = 0
        r = len(height) - 1
        max_area = 0
        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_area = max(area, max_area)
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                # equal heights, can move either
                l += 1
        return max_area


sol = Solution()
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(sol.maxArea([1, 1]))
