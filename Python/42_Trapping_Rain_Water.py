from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left_max = 0
        max_left = []
        for i in range(len(height)):
            max_left.append(left_max)
            if height[i] > left_max:
                left_max = height[i]
        right_max = 0
        max_right = [0] * len(height)
        for j in range(len(height) - 1, -1, -1):
            max_right[j] = right_max
            if height[j] > right_max:
                right_max = height[j]
        min_l_r = [min(l, r) for l, r in zip(max_left, max_right)]

        for k in range(len(height)):
            if min_l_r[k] > height[k]:
                water += min_l_r[k] - height[k]

        return water


sol = Solution()
print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(sol.trap([4,2,0,3,2,5]))
print(sol.trap([4,2,3]))
