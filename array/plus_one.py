class Solution:

    def plusOne(self, digits):
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # no at this index will be 0 and go on to next iteration
            # increment until we find k where k < 9
            digits[i] = 0
        # handle case where all nos = 9
        new_arr = [0] * (n + 1)
        new_arr[0] = 1
        return new_arr


s = Solution()
print(s.plusOne([1, 2, 3]))
print(s.plusOne([4, 3, 2, 1]))
print(s.plusOne([9]))