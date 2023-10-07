from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(selfself, strs: List[str]) -> List[List[str]]:
        # O(m * n)
        # m = num of words,
        # n = average char count of a word which is really about 6 or 7 if it's a real word
        anagram_groups = defaultdict(list)
        for word in strs:
            char_occurrences = [0] * 26 # a ... z
            for char in word:
                # gets number of letter in alphabet by subtracting ascii value of a
                char_occurrences[ord(char) - ord("a")] += 1

            anagram_groups[tuple(char_occurrences)].append(word)

        return list(anagram_groups.values())





solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
