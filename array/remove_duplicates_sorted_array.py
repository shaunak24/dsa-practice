class Solution:

    def removeDuplicates(self, nums) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[k] = nums[i]
                k += 1
        print(nums)
        return k


s = Solution()
print(s.removeDuplicates([1, 1, 2]))
print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
