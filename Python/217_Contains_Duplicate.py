from typing import List, Set


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Iterate through array and store values in a set
        check if element is in the set before storing, if it is than that ele
        has appeared twice
        """
        distinct_elements = set()
        for number in nums:
            if number in distinct_elements:
                return True
            distinct_elements.add(number)

        return False
