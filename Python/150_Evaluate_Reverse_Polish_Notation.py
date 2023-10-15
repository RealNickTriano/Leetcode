from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def performOperation(a: int, b: int, op: str) -> int:
            if op == "+":
                return a + b
            elif op == "-":
                return a - b
            elif op == "*":
                return a * b
            elif op == "/":
                return int(a / b)

        for t in tokens:
            if str.isdigit(t[-1]):
                stack.append(t)
            else:
                # Operator
                first = stack.pop()
                second = stack.pop()
                stack.append(performOperation(int(second), int(first), t))
        return stack[-1]

sol = Solution()
print(sol.evalRPN(["2","1","+","3","*"]))
print(sol.evalRPN(["4","13","5","/","+"]))
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))