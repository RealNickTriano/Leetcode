from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            middle = r + l // 2
            if nums[middle] > target:
                r = middle - 1
            elif nums[middle] < target:
                l = middle + 1
            else:
                return middle

        return -1


sol = Solution()
print(sol.search([-1, 0, 3, 5, 9, 12], 9))
print(sol.search([-1, 0, 3, 5, 9, 12], 2))
print(sol.search([2, 5], 5))
