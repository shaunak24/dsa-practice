class Solution:
    def reverse_two_pt(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def nextPermutation(self, nums) -> None:
        index = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i + 1] > nums[i]:
                index = i
                break
        # print('index', index)
        if index > -1:
            for i in range(len(nums) - 1, index, -1):
                if nums[i] > nums[index]:
                    nums[i], nums[index] = nums[index], nums[i]
                    break
            # print('temp', nums)
            self.reverse_two_pt(nums, index + 1, len(nums) - 1)
        else:   
            nums.reverse()
        print(nums)


s = Solution()
s.nextPermutation([1,2,3]) # 1 3 2
s.nextPermutation([3,2,1]) # 1 2 3
s.nextPermutation([1,1,5]) # 1 5 1
s.nextPermutation([1,3,2]) # 2 1 3
s.nextPermutation([2,3,1]) # 3 1 2
