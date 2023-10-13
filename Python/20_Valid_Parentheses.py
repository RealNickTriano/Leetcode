class Solution():
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) <= 1:
            return False
        for item in s:
            if item == '(':
                stack.append(')')
            elif item == '{':
                stack.append('}')
            elif item == '[':
                stack.append(']')
            else: # Closing paren
                if not stack:
                    return False
                closing = stack.pop()
                if item != closing:
                    return False

        return not stack

sol = Solution()
print(sol.isValid("())()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))
