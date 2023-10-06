class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
            Sort both strings, then they should be equal if anagrams
            O(nlogn + n) -> O(nlogn)

            - create a dict of all letters and increment / decrement their counts
            should all be 0 at the end
            this would be O(n) time but more space
            '
            rat
            '
            car
        """
        if len(s) != len(t):
            return False

        letters = {}

        for i in range(len(s)):
            if letters.get(s[i]) is None:
                letters[s[i]] = 1
            else:
                letters[s[i]] += 1

            if letters.get(t[i]) is None:
                letters[t[i]] = -1
            else:
                letters[t[i]] -= 1

        for k, v in letters.items():
            if v != 0:
                return False

        return True

