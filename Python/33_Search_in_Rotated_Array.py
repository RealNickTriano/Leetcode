from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            print((l, m, r), nums[l], nums[m], nums[r])
            if nums[m] > nums[r]:
                # left part
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    if target >= nums[l]:
                        r = m - 1
                    elif target < nums[l]:
                        l = m + 1
            elif nums[m] < nums[r]:
                # right part
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    if target > nums[r]:
                        r = m - 1
                    elif target <= nums[r]:
                        l = m + 1
            else:
                l = m + 1

        return -1


sol = Solution()
print(sol.search([4, 5, 6, 7, 0, 1, 2], 0))
print(sol.search([4, 5, 6, 7, 0, 1, 2], 3))
print(sol.search([1], 0))
print(sol.search([1,3], 3))
