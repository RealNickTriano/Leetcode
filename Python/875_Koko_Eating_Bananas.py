import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        result = r

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                result = min(result, k)
                r = k - 1
            else:
                l = k + 1

        return result


sol = Solution()
print(sol.minEatingSpeed([3, 6, 7, 11], 8))
print(sol.minEatingSpeed([30, 11, 23, 4, 20], 5))
