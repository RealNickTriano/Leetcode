class Solution:
    def isPalindrome(self, s: str) -> bool:
        # start and end pointer
        # move towards center comparing letters
        # skip non-alphanumerics
        p1 = 0
        p2 = len(s) - 1
        slower = s.lower()
        while p1 < p2:
            if not str.isalnum(s[p1]):
                p1 += 1
            elif not str.isalnum(s[p2]):
                p2 -= 1
            elif slower[p1] != slower[p2]:
                return False
            else:
                p1 += 1
                p2 -= 1

        return True

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
print(sol.isPalindrome("race a car"))
