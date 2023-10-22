from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 0 = nums[i] + nums[j] + nums[k]
        # 0 - nums[i] = nums[j] + nums[k] 2Sum!
        nums.sort()
        res = []
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i - 1]:
                continue
            p1 = i + 1
            p2 = len(nums) - 1
            while p1 < p2:
                if n + nums[p1] + nums[p2] > 0:
                    p2 -= 1
                elif n + nums[p1] + nums[p2] < 0:
                    p1 += 1
                else:
                    # Found triple
                    res.append([n, nums[p1], nums[p2]])
                    p1 += 1
                    while nums[p1] == nums[p1 - 1] and p1 < p2:
                        p1 += 1
        return res

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))