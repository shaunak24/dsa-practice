class Solution:

    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        readPointer, writePointer = 0, 0
        for readPointer in range(len(nums)):
            if nums[readPointer] != 0:
                nums[writePointer], nums[readPointer] = nums[
                    readPointer], nums[writePointer]
                writePointer += 1
        print(nums)


s = Solution()
print(s.moveZeroes([0, 1, 0, 3, 12]))
print(s.moveZeroes([0]))