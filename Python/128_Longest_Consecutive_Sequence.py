import heapq
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_seq = 0
        for n in num_set: # for item in set is much faster than for item in list!!!!!
            if n - 1 not in num_set:
                # start of a sequence
                current_seq = 0
                while n + current_seq in num_set:
                    current_seq += 1
                longest_seq = max(current_seq, longest_seq)

        return longest_seq

sol = Solution()
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(sol.longestConsecutive([0, -1]))
print(sol.longestConsecutive([1,2,0,1]))
