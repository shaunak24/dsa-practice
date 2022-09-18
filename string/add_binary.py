class Solution:

    # One liner 😉
    # def addBinary(self, a: str, b: str) -> str:
    #     return bin(int(a, 2) + int(b, 2))[2:]

    def addBinary(self, a: str, b: str) -> str:
        result = ''
        carry = 0
        a = list(a)
        b = list(b)
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            result += str(carry % 2)
            carry //= 2
        return result[::-1]


s = Solution()
print(s.addBinary('11', '1'))
print(s.addBinary('1010', '1011'))