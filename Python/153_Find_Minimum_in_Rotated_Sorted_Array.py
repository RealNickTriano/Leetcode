from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = 5000

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] <= nums[r]:
                result = min(result, nums[m])
                r = m - 1

        return result


sol = Solution()
print(sol.findMin([3, 4, 5, 1, 2]))
print(sol.findMin([4, 5, 6, 7, 0, 1, 2]))
print(sol.findMin([11, 13, 15, 17]))
