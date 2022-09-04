class Solution:

    def sortArrayByParity(self, nums):
        wp = 0
        for rp in range(len(nums)):
            if nums[rp] % 2 == 0:
                nums[rp], nums[wp] = nums[wp], nums[rp]
                wp += 1
        return nums


s = Solution()
print(s.sortArrayByParity([0]))
print(s.sortArrayByParity([3, 1, 2, 4]))
