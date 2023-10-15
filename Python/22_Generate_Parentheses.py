import math
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def recurse(opened: int, closed: int, result: str):
            if opened == n and closed == n:
                res.append(result)
                return
            if opened < n:
                open_result = result + "("
                recurse(opened + 1, closed, open_result)
            if closed < opened:
                # Add open or closed
                closed_result = result + ")"
                recurse(opened, closed + 1, closed_result)
        recurse(1, 0, "(")
        return res


sol = Solution()
print(sol.generateParenthesis(3))
