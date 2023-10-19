from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        max_h = 0
        for i, h in enumerate(heights):
            last_start = i
            while stack and h < stack[-1][1]:
                start, height = stack.pop()
                max_h = max(max_h, (i - start) * height)
                last_start = start
            stack.append((last_start, h))
        while stack:
            start, height = stack.pop()
            max_h = max(max_h, (len(heights) - start) * height)

        return max_h


sol = Solution()
print(sol.largestRectangleArea([2, 1, 5, 6, 2, 3]))
print(sol.largestRectangleArea([1, 2, 3, 4, 5, 6]))
