class Solution:

    def minSubArrayLen(self, target: int, nums) -> int:
        min_len = float('inf')
        l, r, sum = 0, 0, 0
        while r < len(nums):
            sum += nums[r]
            while sum >= target:
                sum -= nums[l]
                l += 1
                min_len = min((r - l) + 2, min_len)
            r += 1
        return min_len if min_len != float('inf') else 0


s = Solution()
print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(s.minSubArrayLen(4, [1, 4, 4]))
print(s.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
