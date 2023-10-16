from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for i in range(len(temperatures))]
        for idx, t in enumerate(temperatures):
            if stack:
                top = stack[-1]
                while t > top[0]:
                    res[top[1]] = idx - top[1]
                    stack.pop()
                    if not stack:
                        break
                    top = stack[-1]
                stack.append((t, idx))
            else:
                stack.append((t, idx))
        return res

sol = Solution()
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))