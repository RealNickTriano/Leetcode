from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            max_profit = max(max_profit, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            r += 1
        return max_profit


sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
print(sol.maxProfit([7, 6, 4, 3, 1]))
