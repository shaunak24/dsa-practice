class Solution:

    def removeDuplicates(self, nums) -> int:
        writePointer = 1
        for readPointer in range(1, len(nums)):
            if nums[readPointer - 1] != nums[readPointer]:
                nums[writePointer] = nums[readPointer]
                writePointer += 1
        print(nums)
        return writePointer


s = Solution()
print(s.removeDuplicates([1, 1, 2]))
print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
