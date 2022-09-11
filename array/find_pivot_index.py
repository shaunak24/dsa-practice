class Solution:

    def pivotIndex(self, nums) -> int:
        left, right = 0, sum(nums)
        for i in range(len(nums)):
            right -= nums[i]
            if left == right:
                return i
            left += nums[i]
        return -1


s = Solution()
print(s.pivotIndex([1, 7, 3, 6, 5, 6]))
print(s.pivotIndex([1, 2, 3]))
print(s.pivotIndex([2, 1, -1]))
