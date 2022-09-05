class Solution:

    def thirdMax(self, nums) -> int:
        min_int = -1 * 2**31 - 1
        first, second, third = min_int, min_int, min_int
        for n in nums:
            if n == first or n == second or n == third:
                continue
            if n > first:
                third = second
                second = first
                first = n
            elif n > second:
                third = second
                second = n
            elif n > third:
                third = n
        return third if third > min_int else first


s = Solution()
print(s.thirdMax([1, 2, -2147483648]))
# print(s.thirdMax([3, 2, 1]))
# print(s.thirdMax([1, 2]))
# print(s.thirdMax([2, 2, 3, 1]))
