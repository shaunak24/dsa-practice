class Solution:

    def rotate(self, nums, k: int) -> None:

        def reverse(nums, start, end):
            while start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        k %= len(nums)
        n = len(nums)
        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)
        print(nums)


s = Solution()
s.rotate([1, 2, 3, 4, 5, 6, 7], 3)
s.rotate([-1, -100, 3, 99], 2)
s.rotate([1, 2], 1)
s.rotate([1, 2, 3], 2)
