class Solution:

    def arrayPairSum(self, nums) -> int:
        start, end, sum = 0, 1, 0
        nums.sort()
        while end < len(nums):
            sum += min(nums[start], nums[end])
            start += 2
            end += 2
        return sum


s = Solution()
print(s.arrayPairSum([6, 2, 6, 5, 1, 2]))
print(s.arrayPairSum([1, 4, 3, 2]))
