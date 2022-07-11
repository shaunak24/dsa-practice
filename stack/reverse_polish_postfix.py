class Solution:

    def solve(self, a, b, operator):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        else:
            return int(a / b)

    def evalRPN(self, tokens) -> int:
        numbers = []
        for i in tokens:
            if i in ('+', '*', '/', '-'):
                num1 = numbers.pop(-1)
                num2 = numbers.pop(-1)
                numbers.append(self.solve(int(num2), int(num1), i))
            else:
                numbers.append(int(i))
        return numbers[0]


s = Solution()
print(s.evalRPN(["2", "1", "+", "3", "*"]))
print(s.evalRPN(["4", "13", "5", "/", "+"]))
print(
    s.evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
