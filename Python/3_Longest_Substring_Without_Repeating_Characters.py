class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0, 0
        longest = 0
        letters = {}
        while r < len(s):
            if letters.get(s[r]) is not None:
                l = letters.get(s[r]) + 1
                letters = {s[i]: i for i in range(l, r)}
            letters[s[r]] = r
            longest = max((r - l + 1), longest)
            r += 1

        return longest


sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("bbbbb"))
print(sol.lengthOfLongestSubstring("pwwkew"))
print(sol.lengthOfLongestSubstring("dvdf"))
