from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)

        stack = []
        for p, s in pairs:
            time_to_target = (target - p) / s
            if stack:
                if stack[-1] < time_to_target:
                    stack.append(time_to_target)
            else:
                stack.append(time_to_target)

        return len(stack)

sol = Solution()
print(sol.carFleet(10, [3, 5, 7], [3, 2, 1]))
print(sol.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))
print(sol.carFleet(10, [3], [3]))