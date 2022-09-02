from collections import deque


class Solution:

    def sortedSquares(self, nums):
        l, r, ans = 0, len(nums) - 1, deque()
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                ans.appendleft(left**2)
                l += 1
            else:
                ans.appendleft(right**2)
                r -= 1
        return ans


s = Solution()
print(s.sortedSquares([-4, -1, 0, 3, 10]))
print(s.sortedSquares([-7, -3, 2, 3, 11]))
