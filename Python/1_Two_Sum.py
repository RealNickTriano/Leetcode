from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
            the target - num in array will be equal to another number in array
            use dictionary to keep track of what we are actually looking for and the index
        """
        numbers = {}
        for i, n in enumerate(nums):
            if numbers.get(n) is not None:
                return [i, numbers[n]]
            numbers[target - n] = i
