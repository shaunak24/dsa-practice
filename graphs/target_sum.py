# Imagine as a decision tree with (index = 0, total = 0)
# 2 possible child nodes - index + 1, total +- nums[index]


class Solution:

    def findTargetSumWays(self, nums, target: int) -> int:
        dp = {}

        def backtrack(i, total):
            if (i, total) in dp:
                return dp[(i, total)]
            if i == len(nums):
                return 1 if total == target else 0
            dp[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(
                i + 1, total - nums[i])
            return dp[(i, total)]

        return backtrack(0, 0)


s = Solution()
print(s.findTargetSumWays([1, 1, 1, 1, 1], 3))
print(s.findTargetSumWays([1], 1))