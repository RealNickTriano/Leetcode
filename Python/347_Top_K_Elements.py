import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # index = count, values with that count are in the list at that index
        frequencies = [[] for i in range(len(nums) + 1)]
        result = []

        freq = {}
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)

        for key, v in freq.items():
            frequencies[v].append(key)

        for i in range(len(frequencies) - 1, 0, -1):
            for j in frequencies[i]:
                result.append(j)
                if len(result) == k:
                    return result

sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2))