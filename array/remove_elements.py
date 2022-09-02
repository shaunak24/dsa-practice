class Solution:

    def removeElement(self, nums, val):
        length, i = len(nums), 0
        while i < length:
            n = nums[i]
            if n == val:
                nums[i] = nums[length - 1]
                length -= 1
            else:
                i += 1
        print(nums)
        return length


s = Solution()
print(s.removeElement([3, 2, 2, 3], 3))
print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
