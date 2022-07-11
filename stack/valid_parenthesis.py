class Solution:

    def isValid(self, s: str) -> bool:
        pairs = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i in s:
            if i in pairs.keys():
                stack.append(i)
            else:
                if not stack:
                    return False
                c = stack[-1]
                stack = stack[:-1]
                if i != pairs[c]:
                    return False
        if len(stack) > 0:
            return False
        return True


s = Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("{[]}"))
print(s.isValid("{{"))
